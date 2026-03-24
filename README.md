# Biomedical FastAPI App

FastAPI service for biomedical cohort analysis with CSV ingestion, automated chart generation, report + insight authoring, objective-tracking, and a browser gallery/viewer.

## Features

- Upload and validate CSV datasets (`POST /upload/csv`) saved to `data/data.csv`.
- Dataset profiling and descriptive summary (`GET /summary`) including missingness and key distributions.
- Automated chart generation (clinical, biomarker, and survival families) to `output/images`.
- Chart artifact listing and direct image access (`GET /charts`, `GET /charts/{name}`).
- Chart viewer page per artifact (`GET /viewer/{name}`) and image card feed (`GET /output-images`).
- Full pipeline execution (`POST /execute`) to generate charts, report, and insights in one run.
- Markdown report generation and retrieval (`POST /generate/report`, `GET /report`).
- Insight bundle generation (section files + merged markdown + HTML) and retrieval (`POST /generate/insights`, `GET /insights`).
- Research objectives upload/read (`POST /upload/objectives`, `GET /objectives`).
- LLM-generated response-to-objectives document + markdown download (`POST /generate/response-to-objectives`, `GET /response-to-objectives/download`).
- Frontend pages at `/`, `/gallery`, and `/viewer/{name}`.
- Static output serving at `/output/*`.

## Startup Behavior

On every API startup, the app now resets transient output artifacts:

- Empties `output/images/`
- Empties `output/insights/`
- Removes `output/report.md`
- Removes `output/RESPONSE_TO_OBJECTIVES.md`

This keeps each server run clean and prevents stale outputs from prior sessions.

## Architecture

- API routes: `src/biomed_api/api/routes.py`
- App bootstrap/lifespan hooks: `src/biomed_api/main.py`
- Business logic: `src/biomed_api/services/`
- Schemas: `src/biomed_api/models/schemas.py`
- Templates: `src/biomed_api/templates/gallery.html`, `src/biomed_api/templates/viewer.html`

## Environment Variables

- `ANTHROPIC_API_KEY` is required only for `POST /generate/response-to-objectives`.
- No env var is required for chart/report/insight generation and core API usage.

## Run

```bash
uv sync
uv run uvicorn biomed_api.main:app --reload
```

Open:

- API docs: `http://127.0.0.1:8000/docs`
- Dashboard: `http://127.0.0.1:8000/`

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Frontend landing page |
| GET | `/gallery` | Gallery page |
| GET | `/viewer/{name}` | Single-chart viewer page |
| GET | `/health` | Health check |
| POST | `/upload/csv` | Upload + validate dataset |
| GET | `/summary` | Dataset summary/profile |
| POST | `/generate/charts` | Generate standard chart bundle |
| GET | `/charts` | List chart artifacts |
| GET | `/charts/{name}` | Fetch chart image file |
| GET | `/output-images` | List gallery image cards |
| POST | `/generate/report` | Generate `output/report.md` |
| GET | `/report` | Read generated report |
| POST | `/generate/insights` | Generate insights markdown/html bundle |
| GET | `/insights` | Read merged insights markdown |
| POST | `/upload/objectives` | Save `OBJECTIVES.md` content |
| GET | `/objectives` | Read current objectives |
| POST | `/generate/response-to-objectives` | Generate `output/RESPONSE_TO_OBJECTIVES.md` via Anthropic |
| GET | `/response-to-objectives/download` | Download objectives response markdown |
| POST | `/execute` | Run charts + report + insights pipeline |

## Test and Lint

```bash
uv run pytest
uv run ruff check .
uv run ruff format .
```
