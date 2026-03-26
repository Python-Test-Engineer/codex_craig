# Data Intelligence Agent

A Claude Code–powered data intelligence environment built around a FastAPI CSV analysis service.
Upload any CSV and get automated charts, statistical reports, AI-generated insights, and a
searchable SQL query library — all driven by slash commands and autonomous agents.

---

## Quick Start

```bash
uv sync
uv run uvicorn csv_analyser.main:app --reload
```

- API docs: `http://127.0.0.1:8000/docs`
- Gallery:  `http://127.0.0.1:8000/`

---

## CSV Analyser — FastAPI Service

### Architecture

```
src/csv_analyser/
├── main.py                   app bootstrap & lifespan hooks
├── api/routes.py             all endpoints
├── models/schemas.py         Pydantic request/response models
├── services/
│   ├── data_service.py       CSV loading, type coercion, domain detection
│   ├── chart_service.py      Plotly chart generation (6 chart families)
│   ├── dirty_service.py      data quality detection (nulls, dupes, outliers)
│   ├── report_service.py     statistical summary report
│   ├── insight_service.py    LLM-powered per-chart insights (OpenRouter)
│   ├── objectives_service.py LLM response to user-defined objectives
│   └── sql_service.py        in-memory SQLite query execution against uploaded CSV
└── templates/
    ├── gallery.html
    └── viewer.html
```

### Analysis Pipeline

```
POST /upload/csv
    └─► data_service   — normalise columns, coerce types, detect domain
    └─► sql_service    — builds SQL catalog in background (automatic, no LLM needed)
POST /generate/charts
    └─► chart_service  — distributions, correlations, time series, scatter
POST /generate/report
    └─► report_service — numeric summary, top categories, correlations, chart index
POST /generate/insights
    └─► insight_service — per-chart AI commentary → insights.md + insights.html
POST /generate/response-to-objectives
    └─► objectives_service — detailed analytical response to OBJECTIVES.md
                             (uses SQL catalog + insights as primary context)
POST /ask
    └─► OpenRouter — context-aware Q&A grounded in SQL results + insights
POST /execute
    └─► runs charts + report + insights in one call (cancellable via POST /cancel-pipeline)
```

### Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Gallery page |
| GET | `/health` | Health check |
| POST | `/upload/csv` | Upload + validate dataset |
| GET | `/summary` | Dataset profile (schema, missingness, domain) |
| POST | `/generate/charts` | Generate chart bundle (PNG + metadata) |
| GET | `/charts` | List chart artifacts |
| GET | `/charts/{name}` | Fetch chart image |
| GET | `/output-images` | Gallery image cards |
| POST | `/generate/report` | Generate `output/report.md` |
| GET | `/report` | Read generated report |
| POST | `/generate/insights` | Generate per-chart insights + merged HTML |
| GET | `/insights` | Read merged insights |
| POST | `/upload/objectives` | Save `OBJECTIVES.md` content |
| GET | `/objectives` | Read current objectives |
| POST | `/generate/response-to-objectives` | Generate `output/RESPONSE_TO_OBJECTIVES.md` |
| GET | `/response-to-objectives/download` | Download objectives response (Markdown) |
| GET | `/response-to-objectives/download-html` | Download objectives response (HTML) |
| POST | `/ask` | Ask a question grounded in generated insights |
| POST | `/execute` | Run full charts + report + insights pipeline |
| POST | `/cancel-pipeline` | Cancel a running `/execute` pipeline |
| GET | `/sql-status` | Poll SQL catalog build status (`not_started` / `running` / `ready`) |
| GET | `/viewer/{name}` | Single-chart viewer page |
| GET | `/gallery` | Full-page chart gallery |

### Output Lifecycle

On every API startup the app resets transient outputs:

- `output/images/` — emptied
- `output/insights/` — emptied
- `output/report.md` — removed
- `output/dirty.csv` — removed
- `output/dirty_rows.md` — removed
- `output/RESPONSE_TO_OBJECTIVES.md` — removed
- `output/RESPONSE_TO_OBJECTIVES.html` — removed

Files under `output/sql/` are **not** reset — they are durable artifacts produced by the
SQL commands below. They are also protected during pipeline runs: `chart_service.py` uses
`_CLEAN_SKIP = {"sql"}` to prevent `rglob` from deleting any file whose path contains `sql/`.

### Environment Variables

| Variable | Required for |
|---|---|
| `OPENROUTER_API_KEY` | `/generate/insights`, `/generate/response-to-objectives`, `/ask` |

---

## SQL Workflow

The SQL pipeline turns any uploaded CSV into a searchable, executable query library. It
operates in two tiers:

### Tier 1 — Server-side auto-build (always runs, no Claude Code required)

When a CSV is uploaded, `sql_service.py` runs as a FastAPI `BackgroundTask`. It builds a
schema-based query catalog automatically and runs all queries against an in-memory SQLite
database, merging results inline. No LLM key is needed.

```
POST /upload/csv
    └─► sql_service (BackgroundTask)
            ├─► generates output/sql/sql_queries_<table>.md   (SQL + inline results)
            └─► writes output/sql/.status.json                (polled by GET /sql-status)
```

### Tier 2 — Claude sql-agent (LLM-enhanced, optional)

When Claude Code is active and a CSV upload is detected, the `sql-agent` runs
`/sql-titles` + `/sql-create` to produce a richer LLM-authored query catalog with
descriptive titles and business-context-aware queries.

```
POST /upload/csv
    └─► sql-agent (if Claude Code session is active)
            ├─► /sql-titles data/<csv>
            │       └─► output/sql/sql_title.md       (LLM-authored titles + descriptions)
            └─► /sql-create output/sql/sql_title.md
                    ├─► output/sql/sql_queries_<table>.md   (SQL + inline test results)
                    └─► output/sql/log_test_at_sql_queries_<table>.md
```

Both tiers write `output/sql/.status.json`. The gallery UI polls `GET /sql-status` every
2 seconds and shows a live status indicator in the upload card.

Each entry in the query file is structured for instant Grep retrieval:

```markdown
## Total Revenue by Product
**ARGS:** —
**Description:** Ranks each product by total revenue generated, highest first.
```sql
SELECT product_name,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY product_name
ORDER BY total_revenue DESC
```
---
```

---

## Claude Code Commands

### SQL Analysis

| Command | Arguments | Output |
|---|---|---|
| `/sql-titles` | `<csv_file>` | `output/sql/sql_title.md` — query titles with descriptions |
| `/sql-create` | `<sql_title.md> [output_file]` | `output/sql/sql_queries_<table>.md` — full SQL catalog |

### Research Pipeline

| Command | Arguments | Output |
|---|---|---|
| `/planner` | `_ideas/<file>.md` | `_plans/<file>.md` — structured research plan |
| `/spec` | `_plans/<file>.md` | `_specs/<file>.md` — Python technical spec |
| `/execute` | `_specs/<file>.md` | Runs all scripts defined in the spec |
| `/insights` | `<image_folder>` | Per-chart insight files + `insights.md` + `insights.html` |
| `/solve` | `<output_folder> <question>` | Evidence-grounded answer from charts and reports |
| `/dashboard` | `<output_folder>` | Interactive Shiny dashboard |

### Developer Utilities

| Command | Purpose |
|---|---|
| `/uv` | `uv sync` and activate the virtual environment |
| `/commit-message` | Draft a commit message from the current git diff |
| `/show-convo` | Show conversation history |
| `/rsi` | Recursive self-improvement — improve commands/skills/agents |
| `/style` | Select an output style for the conversation |

---

## Agents

| Agent | Trigger | Role |
|---|---|---|
| `sql-agent` | When Claude Code is active and a CSV is uploaded | LLM-enhanced SQL catalog: runs `/sql-titles` → `/sql-create` with business-context queries (supplements the server-side auto-build) |
| `data-cleaner` | Before analysis | Scans dataset for dirty rows: nulls, duplicates, outliers |
| `statistician` | After cleaning | Per-column mean/std, top-performing column, plain-English summary |
| `visualizer` | After statistics | Chart titles and one-sentence visual insights |
| `reporter` | After all agents | Assembles final investigation report in Markdown |
| `code-quality-reviewer` | After `/execute` or on request | Reviews code diff for quality and correctness |

---

## Project Structure

```
src/
  csv_analyser/              main FastAPI service
  biomed_api/                biomedical variant (mirrors csv_analyser structure)
data/                        source CSV datasets
output/
  images/                    generated charts (reset on API startup)
  insights/                  insight files    (reset on API startup)
  sql/                       SQL query library (durable — not reset)
    sql_title.md
    sql_queries_<table>.md
_ideas/                      research idea files  → /planner input
_plans/                      research plans       → /spec input
_specs/                      technical specs      → /execute input
.claude/
  commands/                  slash command definitions
  agents/                    agent definitions
  output-styles/             output formatting styles
```

---

## Test and Lint

```bash
uv run pytest
uv run ruff check .
uv run ruff format .
```
