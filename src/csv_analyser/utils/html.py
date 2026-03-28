"""Shared markdown-to-HTML renderer used by insight_service and objectives_service."""
from __future__ import annotations

import re
from html import escape


def _inline(text: str) -> str:
    """Apply inline markdown (bold, italic, code) to escaped HTML text."""
    out = escape(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\*(.+?)\*", r"<em>\1</em>", out)
    out = re.sub(r"`(.+?)`", r"<code>\1</code>", out)
    return out


def _is_table_separator(line: str) -> bool:
    return bool(re.match(r"^\|[\s\|\-\:]+\|$", line))


def _parse_table_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def render_markdown_to_html(markdown_text: str) -> str:
    """Convert a markdown string to an HTML fragment.

    Supports: headings (h1–h3), bullet lists, tables (with thead/tbody),
    inline bold/italic/code, horizontal rules, and image embeds.
    """
    lines = markdown_text.splitlines()
    html_parts: list[str] = []
    in_list = False
    in_table = False
    table_header_done = False

    def _close_open_blocks() -> None:
        nonlocal in_list, in_table, table_header_done
        if in_list:
            html_parts.append("</ul>")
            in_list = False
        if in_table:
            html_parts.append("</tbody></table>")
            in_table = False
            table_header_done = False

    for raw_line in lines:
        line = raw_line.strip()

        # --- table rows ---
        if line.startswith("|"):
            if _is_table_separator(line):
                if in_table and not table_header_done:
                    html_parts.append("</tr></thead><tbody>")
                    table_header_done = True
                continue

            if not in_table:
                _close_open_blocks()
                html_parts.append("<table>")
                html_parts.append("<thead><tr>")
                for cell in _parse_table_cells(line):
                    html_parts.append(f"<th>{_inline(cell)}</th>")
                in_table = True
                table_header_done = False
            else:
                html_parts.append("<tr>")
                for cell in _parse_table_cells(line):
                    html_parts.append(f"<td>{_inline(cell)}</td>")
                html_parts.append("</tr>")
            continue

        # leaving a table
        if in_table:
            html_parts.append("</tbody></table>")
            in_table = False
            table_header_done = False

        if not line:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            continue

        if line.startswith("---"):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append("<hr />")
            continue

        if line.startswith("### "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h3>{_inline(line[4:])}</h3>")
            continue

        if line.startswith("## "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h2>{_inline(line[3:])}</h2>")
            continue

        if line.startswith("# "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h1>{_inline(line[2:])}</h1>")
            continue

        if line.startswith("![") and "](" in line and line.endswith(")"):
            alt_end = line.find("]")
            src_start = line.find("(", alt_end) + 1
            src = line[src_start:-1]
            alt = line[2:alt_end]
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(
                f'<p><img src="{escape(src)}" alt="{escape(alt)}" '
                f'style="max-width: 100%; border: 1px solid #d0d6dd; border-radius: 10px;" /></p>'
            )
            continue

        if line.startswith("- "):
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append(f"<li>{_inline(line[2:])}</li>")
            continue

        if in_list:
            html_parts.append("</ul>")
            in_list = False

        if line.startswith("_") and line.endswith("_") and len(line) > 2:
            html_parts.append(f"<p><em>{escape(line[1:-1])}</em></p>")
        else:
            html_parts.append(f"<p>{_inline(line)}</p>")

    _close_open_blocks()

    return "\n".join(html_parts)
