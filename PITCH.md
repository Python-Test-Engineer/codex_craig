# From Raw CSV to Boardroom-Ready Intelligence — in Under 60 Seconds

**Addressed to:** Head of Data Intelligence
**Re:** AKD Data Intelligence Platform — CSV Analyser

---

## The Problem You Know Better Than Anyone

Your analysts spend the first two hours of every investigation doing the same thing: loading data, cleaning it, building the first round of charts, writing the summary, and then — finally — starting the actual analysis. That's before a single business question has been answered.

You have smart people doing slow work. And every hour they spend on setup is an hour they are not generating insight.

---

## What AKD CSV Analyser Does

AKD CSV Analyser is a self-contained data intelligence platform. Drop in any CSV. One click. It produces the full analytical stack automatically — in the time it takes to make a coffee.

### The Pipeline (what runs in a single click)

| Step | What it produces |
|------|-----------------|
| **Data ingestion** | Automatic type coercion, column normalisation, encoding detection |
| **Data quality audit** | Dirty-row detection with per-row reason codes — exported as `dirty.csv` and a human-readable markdown report |
| **Chart generation** | A comprehensive set of statistical charts — distributions, correlations, category breakdowns, time-series — as publication-ready PNGs |
| **Statistical report** | Narrative markdown report: dataset snapshot, numeric summaries, top distributions, correlations, and caveats |
| **AI chart insights** | Every chart is read by an LLM, which writes three-part insight cards: *what the data shows*, *what it means*, and *what to watch for* |
| **SQL query catalog** | The platform inspects the schema and auto-generates 25–40 executable SQL queries across categories — summaries, rankings, distributions, time trends, parametric lookups, and data quality checks — ready to run against a live SQLite database |

Zero code written. Zero configuration required. No API key needed for the core pipeline.

---

## The Intelligence Layer — Ask AI

After the pipeline runs, your team can interrogate the data in plain English through the **Ask AI** interface.

This is not a chatbot bolted onto a spreadsheet. The system is architecturally grounded:

1. **It consults the SQL catalog first.** The LLM selects the best pre-generated query for the question, executes it against a live SQLite database, and returns real row-level results.
2. **It draws on chart insights second.** Visual patterns, trends, and anomalies captured during chart analysis provide qualitative context the numbers alone cannot.
3. **It never touches the raw CSV.** Token efficiency is preserved. The model works from curated, structured intelligence — not a wall of data.

Every answer cites its source: the exact file, line range, and query title used. Reproducible. Auditable. Trustworthy.

---

## Objectives-Driven Analysis

Before the pipeline runs, your team can define research objectives in plain language:

```
What is driving the decline in average order value in Q4?
Which product categories have the highest return rates?
Are there regional patterns in customer churn?
```

The platform maps every pipeline output — charts, statistics, insights — against each objective and returns a structured response: *evidence found*, *gaps identified*, *recommended next analyses*. Delivered as a formatted HTML report, downloadable in one click.

This is the difference between analysis that answers what you asked and analysis that answers what you should have asked.

---

## What Your Team Gets Back

Every pipeline run produces a self-contained intelligence package:

- `output/images/` — all charts as PNGs
- `output/insights/insights.md` + `.html` — AI-generated insight report, per chart and consolidated
- `output/report.md` — statistical narrative
- `output/dirty.csv` + `dirty_rows.md` — data quality audit
- `output/sql/sql_title.md` — natural-language SQL catalog
- `output/sql/sql_queries_<dataset>.md` — 25–40 executable queries
- `output/sql/data.db` — live SQLite database, query-ready
- `output/RESPONSE_TO_OBJECTIVES.md` + `.html` — objectives response report

Everything is markdown or HTML. Everything is downloadable. Nothing is locked in a proprietary format.

---

## Designed for Data Teams

- **No-code interface** — the web dashboard covers the full workflow; no terminal required
- **API-first** — every action is a REST endpoint; integrate into existing pipelines trivially
- **LLM-agnostic** — runs on any OpenRouter-compatible model; swap models via a single environment variable
- **Offline capable** — charts, reports, SQL catalog, and data quality audit run entirely without an API key
- **Auditable by design** — every AI output cites its source with filename and line number

---

## The Business Case in One Paragraph

A senior analyst costs £80–120k per year. At eight productive hours per day, that is £45–67 per hour. The AKD CSV Analyser eliminates two to four hours of setup work per investigation. At five investigations per analyst per week, across a team of ten, that is **400–800 analyst-hours recovered per year** — before accounting for the quality uplift from systematic data quality auditing and AI-grounded insight generation that human workflows routinely skip under time pressure.

The platform does not replace your analysts. It removes the part of their job they were never hired to do.

---

## Next Step

We would welcome the opportunity to run a live demonstration on one of your own datasets — no preparation required on your side. Bring a CSV. We will have a full intelligence report on your screen within two minutes.

---

*AKD Data Intelligence Platform*
*Built with FastAPI · pandas · Plotly · OpenRouter · Claude*
