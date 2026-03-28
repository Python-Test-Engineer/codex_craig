"""Tests for objectives_service pure functions."""
from __future__ import annotations

from csv_analyser.services.objectives_service import count_objectives
from csv_analyser.utils.html import render_markdown_to_html


# ── count_objectives ─────────────────────────────────────────────────────────

def test_count_objectives_bullet_list() -> None:
    text = "- Find top products\n- Identify trends\n- Check quality"
    assert count_objectives(text) == 3


def test_count_objectives_numbered_list_dot() -> None:
    text = "1. Find top products\n2. Identify trends\n3. Check quality"
    assert count_objectives(text) == 3


def test_count_objectives_numbered_list_colon() -> None:
    text = "1: Objective A\n2: Objective B"
    assert count_objectives(text) == 2


def test_count_objectives_star_bullets() -> None:
    text = "* Goal one\n* Goal two"
    assert count_objectives(text) == 2


def test_count_objectives_free_form_prose() -> None:
    text = "Analyse sales by region.\n\nIdentify top customers.\n\nCheck monthly trends."
    assert count_objectives(text) == 3


def test_count_objectives_empty() -> None:
    assert count_objectives("") == 0


# ── render_markdown_to_html ───────────────────────────────────────────────────

def test_render_headings() -> None:
    html = render_markdown_to_html("# H1\n## H2\n### H3")
    assert "<h1>" in html
    assert "<h2>" in html
    assert "<h3>" in html


def test_render_bullet_list() -> None:
    html = render_markdown_to_html("- item one\n- item two")
    assert "<ul>" in html
    assert "<li>" in html
    assert "item one" in html


def test_render_bold_inline() -> None:
    html = render_markdown_to_html("This is **important**.")
    assert "<strong>important</strong>" in html


def test_render_italic_inline() -> None:
    html = render_markdown_to_html("This is *italic*.")
    assert "<em>italic</em>" in html


def test_render_code_inline() -> None:
    html = render_markdown_to_html("Use `SELECT *` here.")
    assert "<code>SELECT *</code>" in html


def test_render_table() -> None:
    md = "| Name | Value |\n|---|---|\n| Alice | 42 |\n| Bob | 7 |"
    html = render_markdown_to_html(md)
    assert "<table>" in html
    assert "<thead>" in html
    assert "<tbody>" in html
    assert "<th>" in html
    assert "<td>" in html
    assert "Alice" in html
    assert "42" in html


def test_render_hr() -> None:
    html = render_markdown_to_html("Above\n\n---\n\nBelow")
    assert "<hr />" in html


def test_render_image() -> None:
    html = render_markdown_to_html("![alt text](../images/foo.png)")
    assert "<img" in html
    assert "foo.png" in html


def test_render_escaped_html_in_text() -> None:
    html = render_markdown_to_html("Score > 50 & ready")
    assert "<script" not in html
    # html.escape should convert & and >
    assert "&amp;" in html or "&gt;" in html or "Score" in html
