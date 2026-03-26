---
description: "Read a sql_title.md file and generate SQL for every query title in it, save to output/sql/sql_queries_<table>.md, then run tests inline via Bash and merge results. Usage: /sql-create <sql_titles_file> [output_filename]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash, Skill
argument-hint: "output/sql/sql_title.md"
---

**Arguments:**
- `SQL_TITLES_FILE` — path to a sql_title.md file produced by `/sql-titles` (first token)
- `OUTPUT_FILE` — filename to save results to, without path (second token, optional)

Examples:
```
/sql-create output/sql/sql_title.md
/sql-create output/sql/sql_title.md my_queries.md
```

Parse `$ARGUMENTS`:
- `SQL_TITLES_FILE` — first token
- `OUTPUT_FILE` — second token (optional)

**If `SQL_TITLES_FILE` is missing:**
Glob `output/sql/*.md`, filter for files whose name contains `sql_title`, list them, and ask
the user to pick one.

---

## Your role

You are a senior SQL analyst. Your job is to read every query title from a catalog file and
produce a precise, correct SQL query for each one — writing all results to a single markdown
file that Claude can search and retrieve from instantly.

---

## Step 1 — Load dataset context

1. **Glob** `data/*.csv` — use the first match as the source table
2. **Read** the first 3 lines of that CSV to extract the header row (column names)
3. **Read** `SQL_TITLES_FILE` in full — this is both the source of titles AND additional
   context about the dataset's entities and measures

Derive:
- `TABLE_NAME` — CSV filename minus `.csv`, spaces/hyphens replaced with underscores
  (e.g. `sales_data_100.csv` → `sales_data_100`)
- `OUTPUT_FILE` — if not provided by the user, default to `sql_queries_<TABLE_NAME>.md`
- `OUTPUT_PATH` — always `output/sql/<OUTPUT_FILE>`

---

## Step 2 — Extract all query titles and descriptions

Parse `SQL_TITLES_FILE` to extract every numbered entry. Entries appear in two possible formats:

**With description** (produced by current `/sql-titles`):
```
1. Total Sales Revenue — Shows the combined sum of all order revenue across the entire dataset.
2. Total Revenue by Product — Ranks each product by total revenue generated, highest first.
```

**Title only** (produced by older `/sql-titles` runs):
```
1. Total Sales Revenue
2. Total Revenue by Product
```

For each entry extract:
- `TITLE` — text before ` — ` (or the full line if no ` — ` present), stripped of the leading number and period
- `DESCRIPTION` — text after ` — ` if present; otherwise leave blank and generate one in Step 3

Preserve the section groupings — you will use them to organise the output file.

Tell the user how many titles were found before proceeding.

---

## Step 3 — Generate SQL and description for every title

Work through every title in order. For each one, produce:

**SQL** — a single query following these rules:
- Use only column names present in the CSV header
- Use `TABLE_NAME` as the FROM target
- Write standard ANSI SQL (compatible with SQLite, DuckDB, PostgreSQL)
- Use `ORDER BY` where a ranked or sorted result is implied
- Use `LIMIT` only where explicitly implied (e.g. "Top 5 …")
- For titles with a variable entity (e.g. "Revenue for Customer X", "Units Sold by Product"),
  use a named placeholder: `WHERE column = :param_name` — record `param_name` as an ARG
- `ARGS` — comma-separated placeholder names, or `—` if none

**Description** — use the `DESCRIPTION` extracted from `SQL_TITLES_FILE` if present.
If the titles file had no description for this entry, generate one following these rules:
- One sentence, max 20 words
- Start with a verb: `Shows`, `Returns`, `Ranks`, `Identifies`, `Compares`, `Flags`, `Lists`
- Name the specific metric **and** dimension (e.g. "total revenue per product", not just "revenue")
- Be distinct enough that Claude can select the right query from a user's natural-language question

Process all titles before writing. Do not write the file incrementally.

---

## Step 4 — Write `OUTPUT_PATH`

Write the complete file in one operation using the **Write** tool.

### File structure

```markdown
# SQL Query Catalog
<!-- source: <CSV_FILE> | table: <TABLE_NAME> | generated: <YYYY-MM-DD> | queries: <N> -->

---

### <Section name from sql_title.md>

## <Query Title 1>
**ARGS:** <args or —>
**Description:** <one-sentence description>
```sql
<SQL>
```
---

## <Query Title 2>
**ARGS:** <args or —>
**Description:** <one-sentence description>
```sql
<SQL>
```
---
```

### Format rules (critical for fast AI retrieval)

- Every query title is a `##` heading — this is the Grep key. `Grep pattern: "## Total Revenue by Product"` returns exactly one match.
- `**ARGS:**` is always line 1 directly below the `##` heading.
- `**Description:**` is always line 2, immediately after `**ARGS:**` — no blank line between them.
- SQL is always inside a fenced ` ```sql ` block on the very next line after `**Description:**`.
- Every entry is closed with a `---` horizontal rule on its own line, no blank line before it.
- Section headings from the source file appear as `###` headings to visually group queries without conflicting with the `##` query-title grep key.
- Keep the entire entry tight — no extra blank lines anywhere inside `**ARGS:**` / `**Description:**` / code block / `---`.

---

## Step 5 — Run tests via Bash

Run the two Python blocks below directly with Bash (substituting `OUTPUT_PATH` for
`QUERIES_FILE`). Do **not** call `/sql-test` via the Skill tool — nested Skill invocations
are not reliable. Run these scripts yourself.

**Script A — execute queries and write log file** (`log_test_at_<table>.md`):

```bash
uv run python - <<'PYEOF'
import sqlite3, pandas as pd, pathlib, re as _re

queries_file = pathlib.Path("QUERIES_FILE")
_header_text = queries_file.read_text(encoding="utf-8")

_src_match  = _re.search(r"<!--.*?source:\s*(\S+?)[\s|]", _header_text)
_tbl_match  = _re.search(r"<!--.*?table:\s*(\S+?)[\s|]",  _header_text)

csv_path       = pathlib.Path(_src_match.group(1)) if _src_match else pathlib.Path("data/data.csv")
_catalog_table = _tbl_match.group(1).rstrip("|").strip() if _tbl_match else csv_path.stem.lower()

if not csv_path.exists() and csv_path.parent == pathlib.Path("."):
    csv_path = pathlib.Path("data") / csv_path

if not csv_path.exists():
    raise SystemExit(f"CSV not found: {csv_path}")

df = pd.read_csv(csv_path)
con = sqlite3.connect(":memory:")
df.to_sql(_catalog_table, con, if_exists="replace", index=False)
con.row_factory = sqlite3.Row
print(f"Loaded {len(df)} rows into in-memory table '{_catalog_table}' from {csv_path}")

entries = []
current_title = None
in_sql = False
sql_lines = []

for line in _header_text.splitlines():
    stripped = line.strip()
    if stripped.startswith("## ") and not stripped.startswith("### "):
        if current_title and sql_lines:
            entries.append({"title": current_title, "sql": "\n".join(sql_lines).strip()})
        current_title = stripped[3:].strip()
        sql_lines = []
        in_sql = False
    elif stripped == "```sql":
        in_sql = True
    elif stripped == "```" and in_sql:
        in_sql = False
    elif in_sql:
        sql_lines.append(line)

if current_title and sql_lines:
    entries.append({"title": current_title, "sql": "\n".join(sql_lines).strip()})

results = []
for entry in entries:
    title = entry["title"]
    sql   = entry["sql"]
    if ":" in sql and any(f":{w}" in sql for w in sql.split(":")):
        results.append({"title": title, "sql": sql, "status": "skipped",
                        "reason": "Query requires runtime arguments (:param)", "rows": []})
        continue
    try:
        cur = con.execute(sql)
        cols = [d[0] for d in cur.description] if cur.description else []
        rows = [dict(zip(cols, row)) for row in cur.fetchall()]
        results.append({"title": title, "sql": sql, "status": "ok", "columns": cols, "rows": rows})
    except Exception as e:
        results.append({"title": title, "sql": sql, "status": "error", "reason": str(e), "rows": []})

con.close()

lines = []
lines.append("# SQL Test Results")
lines.append(f"\nQueries file: `{queries_file}`  ")
lines.append(f"Source CSV: `{csv_path}` (in-memory SQLite)  ")
lines.append(f"Queries run: **{len(results)}** (all)\n")
lines.append("---\n")

passed  = sum(1 for r in results if r["status"] == "ok")
failed  = sum(1 for r in results if r["status"] == "error")
skipped = sum(1 for r in results if r["status"] == "skipped")
lines.append(f"**Summary:** {passed} passed · {failed} failed · {skipped} skipped\n")
lines.append("---\n")

for i, r in enumerate(results, 1):
    lines.append(f"## {i}. {r['title']}")
    lines.append(f"\n**Status:** {r['status'].upper()}\n")
    lines.append("```sql")
    lines.append(r["sql"])
    lines.append("```\n")
    if r["status"] == "ok":
        rows = r["rows"]
        cols = r.get("columns", [])
        lines.append(f"**Rows returned:** {len(rows)}\n")
        if rows:
            lines.append("| " + " | ".join(cols) + " |")
            lines.append("| " + " | ".join("---" for _ in cols) + " |")
            for row in rows[:20]:
                cells = [str(row.get(c, "")) for c in cols]
                lines.append("| " + " | ".join(cells) + " |")
            if len(rows) > 20:
                lines.append(f"\n*…{len(rows) - 20} more rows not shown*")
        else:
            lines.append("*(no rows returned)*")
    elif r["status"] == "error":
        lines.append(f"**Error:** `{r['reason']}`")
    else:
        lines.append(f"**Skipped:** {r['reason']}")
    lines.append("\n---\n")

output = queries_file.with_name("log_test_at_" + queries_file.stem + ".md")
output.write_text("\n".join(lines), encoding="utf-8")
print(f"Written: {output}  ({passed} passed, {failed} failed, {skipped} skipped)")
PYEOF
```

**Before running Script A**, replace `QUERIES_FILE` with the actual `OUTPUT_PATH`.

**Script B — merge results inline into the queries file:**

```bash
uv run python - <<'PYEOF'
import pathlib, re

queries_file = pathlib.Path("QUERIES_FILE")
results_file = queries_file.with_name("log_test_at_" + queries_file.stem + ".md")

queries_text = queries_file.read_text(encoding="utf-8")
results_text = results_file.read_text(encoding="utf-8")

result_map = {}
result_blocks = re.split(r'\n(?=## \d+\.)', results_text)
for block in result_blocks:
    m = re.match(r'## \d+\.\s+(.+)', block)
    if not m:
        continue
    title = m.group(1).strip()
    status_m = re.search(r'\*\*Status:\*\*\s+(\S+)', block)
    status = status_m.group(1) if status_m else "UNKNOWN"
    after_sql = re.split(r'```\n', block, maxsplit=2)
    result_body = after_sql[-1].strip() if len(after_sql) >= 2 else ""
    result_body = re.sub(r'\n---\s*$', '', result_body).strip()
    result_map[title] = {"status": status, "body": result_body}

lines = queries_text.splitlines()
out = []
i = 0
current_title = None
in_sql = False
skip_old_results = False

while i < len(lines):
    line = lines[i]
    stripped = line.strip()
    if stripped.startswith("## ") and not stripped.startswith("### "):
        current_title = stripped[3:].strip()
        skip_old_results = False
    if stripped == "```sql":
        in_sql = True
        skip_old_results = False
        out.append(line)
        i += 1
        continue
    if stripped == "```" and in_sql:
        in_sql = False
        skip_old_results = True
        out.append(line)
        if current_title and current_title in result_map:
            r = result_map[current_title]
            out.append("")
            out.append(f"**Status:** {r['status']}")
            if r["body"]:
                out.append("")
                out.append(r["body"])
        i += 1
        continue
    if skip_old_results and (stripped == "---" or stripped.startswith("## ") or stripped.startswith("### ")):
        skip_old_results = False
    if skip_old_results:
        i += 1
        continue
    out.append(line)
    i += 1

queries_file.write_text("\n".join(out), encoding="utf-8")
print(f"Merged {len(result_map)} results into {queries_file}")
PYEOF
```

**Before running Script B**, replace `QUERIES_FILE` with the actual `OUTPUT_PATH`.

---

## Step 6 — Confirm

Tell the user:

```
Generated : <N> SQL queries
Table     : <TABLE_NAME>
Saved to  : <OUTPUT_PATH>
Tested    : <passed> passed · <failed> failed · <skipped> skipped
```

Then list each section name and the count of queries in it, e.g.:
```
  Revenue & Sales       9 queries
  Volume & Orders       7 queries
  ...
```

Do not print the SQL — the file contains everything.
