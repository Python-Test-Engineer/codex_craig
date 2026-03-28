# CSV Analyser — Recommendations

> Review date: 2026-03-28. All file:line references are relative to `src/csv_analyser/`.

The app has a solid feature set — upload-to-insights pipeline, SQL catalog, AI Q&A, and a clean single-page dashboard. The recommendations below are prioritised from blockers down to polish. Each item includes a severity tag and a concrete suggested fix.

---

## 1. Critical Bugs

### 1.1 — [CRITICAL] Entire test suite imports from a deleted package DONE

All five test files (`tests/test_api_routes.py`, `test_data_service.py`, `test_chart_service.py`, `test_insight_service.py`, `test_report_service.py`) import from `biomed_api.*` — an old project name — rather than `csv_analyser.*`. They also assert for strings like `"Biomedical FastAPI Frontend"`, `"Final Biomedical Insights"`, and `"Cohort Snapshot"` that no longer exist. Every test fails on import.

**Fix:** Replace all `biomed_api` imports with `csv_analyser`, update assertion strings to match current templates/output, and re-run `uv run pytest` to confirm green.

---

## 2. Code Quality

### 2.1 — [High] `_safe_category_from_name` duplicated

The function is copy-pasted verbatim between `api/routes.py:118` and `services/chart_service.py:19`.

**Fix:** Delete the copy in `routes.py` and import the one from `chart_service`:
```python
from csv_analyser.services.chart_service import _safe_category_from_name
```

### 2.2 — [High] `_render_markdown_to_html` duplicated with diverging behaviour

`services/insight_service.py:279` and `services/objectives_service.py:71` each contain their own markdown-to-HTML renderer. The objectives version supports inline bold/italic/code and tables; the insight version does not. Divergence will grow.

**Fix:** Extract a shared `utils/html.py` module with the richer objectives-service implementation and import it in both services.

### 2.3 — [Medium] `asyncio.get_event_loop()` is deprecated

Used in `ask_question` (`routes.py:516`) and `generate_response_to_objectives_endpoint` (`routes.py:271`). In Python 3.10+ this raises a `DeprecationWarning` inside an already-running async context.

**Fix:** Replace with `asyncio.get_running_loop()` which is safe inside `async def` handlers.

### 2.4 — [Medium] Inline module imports inside function bodies

`routes.py` defers `import asyncio`, `import os`, `import httpx`, `import datetime` into function bodies. This hides dependencies, confuses linters, and re-executes on every call.

**Fix:** Move all imports to the top of `routes.py`.

### 2.5 — [Medium] Silent chart failure swallows errors

`chart_service.py:191`:
```python
except Exception:
    pass
```
A chart that fails to render is silently skipped. The pipeline returns success even if every chart failed.

**Fix:** At minimum, log the failure with `logging.warning("Chart %s failed: %s", name, exc)`. Optionally collect failures and include them in `ChartGenerationResponse`.

### 2.6 — [Low] `_dataset_snapshot` and `_dataset_context_for_prompt` overlap

Both functions in `insight_service.py` compute dataset metadata (row count, column count, numeric stats) with slightly different output shapes. Neither is reused from `data_service.build_summary`.

**Fix:** Route both through `data_service.build_summary` or a shared helper to keep dataset metadata logic in one place.

---

## 3. Architecture & Design

### 3.1 — [High] Relative path globals break with non-root CWD

`DATA_PATH = Path("data/data.csv")` and `OUTPUT_DIR = Path("output")` appear independently in `data_service.py`, `chart_service.py`, `dirty_service.py`, `report_service.py`, and `main.py`. They resolve against the process CWD. The `--app-dir src` flag in `START.md` can shift the CWD, making paths silently wrong.

**Fix:** Anchor all paths to the project root using a single shared constant:
```python
# src/csv_analyser/config.py
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = PROJECT_ROOT / "data" / "data.csv"
OUTPUT_DIR = PROJECT_ROOT / "output"
```
Import `DATA_PATH` and `OUTPUT_DIR` from `config` in every service.

### 3.2 — [High] No structured logging

No `logging` calls exist anywhere. Errors reach the HTTP layer as untagged exceptions. In production, diagnosing pipeline failures requires attaching a debugger.

**Fix:** Add `import logging; logger = logging.getLogger(__name__)` to each service and replace silent `pass` blocks and bare `print` calls with `logger.warning` / `logger.error`. Configure log level via an env var in `main.py`.

### 3.3 — [Medium] `generate_response_to_objectives` is non-streaming and uncancellable

`objectives_service.py:285` calls `client.messages.create()` — a blocking call that can run for 30–60 seconds with no way to cancel it mid-flight. `insight_service.py` already solved this correctly with `client.messages.stream()` + a `cancel_event` check per chunk.

**Fix:** Convert `generate_response_to_objectives` to use `client.messages.stream()` and accept a `cancel_event: threading.Event | None` parameter, matching the pattern in `insight_service._call_streaming`.

### 3.4 — [Medium] Two LLM models with no shared configuration

Insights uses `anthropic/claude-3.5-sonnet` (`insight_service.py:26`); objectives uses `minimax/minimax-m2.5:free` (`objectives_service.py:24`). There is no single env var to switch both simultaneously.

**Fix:** Add `OPENROUTER_INSIGHTS_MODEL` and `OPENROUTER_OBJECTIVES_MODEL` env vars (with current model strings as defaults). Document them in `.env.example`.

### 3.5 — [Medium] `execute_plan` is synchronous and holds a global lock

The `/execute` route is a synchronous FastAPI endpoint that holds `_pipeline_running = True` for the entire duration. A second HTTP request blocks. In async FastAPI, sync route functions run in a threadpool, but the global lock is still process-wide — no per-user or per-session isolation.

**Fix:** For single-user use this is acceptable short-term, but adding a `background_tasks`-based pipeline with SSE (Server-Sent Events) for progress updates would remove the blocking behaviour and enable step-by-step feedback (see 5.1).

### 3.6 — [Low] `OPENROUTER_API_KEY` validation deferred to request time

Missing key is detected only when the first LLM endpoint is called, producing a 400 error with no startup warning.

**Fix:** Add a startup check in `main.py`:
```python
import os, logging
if not os.environ.get("OPENROUTER_API_KEY"):
    logging.warning("OPENROUTER_API_KEY is not set — AI features will be unavailable.")
```

---

## 4. Security

### 4.1 — [High] File upload has no size limit

`/upload/csv` reads the entire file content into memory (`content = await file.read()`) with no byte cap. A 500 MB CSV would OOM the server.

**Fix:** Add a size guard immediately after reading:
```python
MAX_UPLOAD_BYTES = 50 * 1024 * 1024  # 50 MB
if len(content) > MAX_UPLOAD_BYTES:
    raise HTTPException(status_code=413, detail="File exceeds 50 MB limit.")
```

### 4.2 — [Medium] File upload validated by extension only

`file.filename.lower().endswith(".csv")` can be trivially bypassed. A file named `exploit.csv` containing HTML/script content would be stored and later served.

**Fix:** After parsing, verify the DataFrame has at least one column and at least one row. Also check `file.content_type` is `text/csv` or `application/octet-stream`.

### 4.3 — [Low] No CORS policy

FastAPI's default allows all origins. If this app is ever deployed behind a reverse proxy or consumed by a browser from a different origin, explicit CORS control is needed.

**Fix:** Add `CORSMiddleware` in `main.py` with an allowlist controlled by an env var:
```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:8001"], ...)
```

---

## 5. UX & Missing Features

### 5.1 — [High] No pipeline step progress feedback

The frontend shows a single spinner for the entire pipeline duration (charts → dirty report → statistical report → insights). Users have no indication of which step is running or how far along it is.

**Fix:** Add a `GET /pipeline-status` polling endpoint (similar to `/sql-status`) that returns `{"step": "generating_charts", "step_index": 1, "total_steps": 4}`. Update the pipeline to write this file between steps. Poll it from the frontend every 1–2 s.

### 5.2 — [Medium] No CSV data preview endpoint

After upload, the user sees only aggregate stats (row count, column count). There is no way to verify the data loaded correctly before running the full pipeline.

**Fix:** Add `GET /preview?rows=10` that returns the first N rows as a JSON array. Display it in the dashboard below the upload stats.

### 5.3 — [Medium] Unanswered questions log not surfaced

`routes.py:641` writes questions that the AI couldn't answer to `output/sql/unanswered_questions.md`, but there is no API endpoint or UI element that exposes this file.

**Fix:** Add `GET /unanswered-questions` that returns the file content (or an empty string if it doesn't exist). Show a badge/count in the Ask section of the dashboard when unanswered questions exist.

### 5.4 — [Medium] `/ask` is fully stateless — no conversation history

Each question is answered independently. Users cannot ask follow-up questions like "expand on that" or "give me the top 5 instead of 3."

**Fix:** Accept an optional `history: list[{role, content}]` field in `AskRequest`. Prepend previous turns to the messages array sent to the LLM, capped at the last 5 exchanges to limit token usage.

### 5.5 — [Low] Gallery has no per-chart download button

Charts can be viewed in the viewer but cannot be saved individually from the UI. Users must navigate to `/output/images/<name>.png` manually.

**Fix:** Add a download link (`<a href="/output/images/{name}" download>`) below each gallery tile in `gallery.html`.

### 5.6 — [Low] Charts are always monthly aggregates for time series

`chart_service.py:143` always aggregates to `"M"` (monthly) period. For datasets spanning only a few days this produces a single-point line chart.

**Fix:** Detect the date range and select the period automatically:
- < 90 days → daily (`"D"`)
- 90 days – 2 years → monthly (`"M"`)
- > 2 years → quarterly (`"Q"`)

---

## 6. Test Coverage Gaps

| Service | Current coverage | Priority |
|---|---|---|
| `dirty_service.py` | No tests | High |
| `sql_service.py` | No tests | High |
| `objectives_service.py` | No tests | Medium |
| `chart_service.py` | Partial (generate + list) | Medium |
| `insight_service.py` | Only LLM-disabled path | Low |

### 6.1 — [High] `dirty_service.py` has no tests

`find_dirty_rows` covers four distinct criteria (missing, duplicate, outlier, negative). None are tested.

**Fix:** Add `tests/test_dirty_service.py` with one parametrised test per criterion plus an "all clean" baseline.

### 6.2 — [High] `sql_service.py` has no tests

`generate_sql_catalog` and `run_tests_and_merge` are the backbone of the SQL feature. No regression coverage exists.

**Fix:** Add `tests/test_sql_service.py` using a minimal in-memory DataFrame. Assert that `sql_title.md` and `sql_queries_*.md` are created with expected sections.

### 6.3 — [Medium] `objectives_service.py` has no tests

`count_objectives` (bullet, numbered, prose formats) and `_render_markdown_to_html` (tables, bold, italic) are pure functions that are straightforward to test without an API key.

**Fix:** Add `tests/test_objectives_service.py` covering each `count_objectives` format and the HTML renderer's table/inline-markup paths.

---

## Summary Table

| # | Area | Severity | Effort |
|---|---|---|---|
| 1.1 | Broken test imports (biomed_api) | Critical | Low |
| 2.1 | `_safe_category_from_name` duplication | High | Low |
| 2.2 | `_render_markdown_to_html` duplication | High | Medium |
| 2.3 | `get_event_loop()` deprecation | Medium | Low |
| 2.4 | Inline imports | Medium | Low |
| 2.5 | Silent chart failure | Medium | Low |
| 3.1 | Relative path globals | High | Medium |
| 3.2 | No structured logging | High | Medium |
| 3.3 | Non-streaming objectives call | Medium | Medium |
| 3.4 | Two disconnected LLM model configs | Medium | Low |
| 3.5 | Blocking global pipeline lock | Medium | High |
| 3.6 | API key validation deferred | Low | Low |
| 4.1 | No upload size limit | High | Low |
| 4.2 | Extension-only file validation | Medium | Low |
| 4.3 | No CORS policy | Low | Low |
| 5.1 | No pipeline step progress | High | Medium |
| 5.2 | No CSV preview endpoint | Medium | Low |
| 5.3 | Unanswered questions not surfaced | Medium | Low |
| 5.4 | Stateless `/ask` endpoint | Medium | Medium |
| 5.5 | No per-chart download | Low | Low |
| 5.6 | Time-series always monthly | Low | Low |
| 6.1 | No tests for dirty_service | High | Low |
| 6.2 | No tests for sql_service | High | Medium |
| 6.3 | No tests for objectives_service | Medium | Low |
