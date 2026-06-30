#!/usr/bin/env python3
"""Validate hydraulic template_follow_map.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_COLUMNS = [
    "Row ID",
    "Exemplar Anchor",
    "Exemplar Unit Function",
    "Followable Move",
    "Must Replace / Prohibited Transfer",
    "User/Task Evidence Anchor",
    "Target Landing Place",
    "Handling Status",
    "Reason / Final Check",
]

VALID_STATUSES = {
    "follow",
    "rebuild_with_user_data",
    "style_only",
    "not_applicable",
    "conflict",
    "needs_confirmation",
}

EVIDENCE_REQUIRED = {"follow", "rebuild_with_user_data"}
REASON_REQUIRED = {"not_applicable", "conflict", "needs_confirmation"}
EMPTY_MARKERS = {"", "-", "—", "NA", "N/A", "无", "none", "None", "待定"}


def split_row(line: str) -> list[str]:
    line = line.strip()
    if not line.startswith("|") or not line.endswith("|"):
        return []
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in line[1:-1]:
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
            escaped = False
            continue
        current.append(char)
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    cells.append("".join(current).strip())
    return cells


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def is_empty(value: str) -> bool:
    return value.strip() in EMPTY_MARKERS


def parse_table(text: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = [line for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        raise ValueError("No Markdown table with data rows found.")
    header = split_row(lines[0])
    if not header:
        raise ValueError("The first table row is not parseable.")
    rows: list[dict[str, str]] = []
    for line in lines[1:]:
        cells = split_row(line)
        if not cells or is_separator(cells):
            continue
        if len(cells) != len(header):
            raise ValueError(f"Row has {len(cells)} cells but header has {len(header)}: {line}")
        rows.append(dict(zip(header, cells)))
    return header, rows


def validate(path: Path) -> tuple[str, list[str]]:
    text = path.read_text(encoding="utf-8-sig")
    header, rows = parse_table(text)
    findings: list[str] = []

    missing = [column for column in REQUIRED_COLUMNS if column not in header]
    if missing:
        findings.append("FAIL missing required columns: " + ", ".join(missing))
        return "FAIL", findings
    if not rows:
        findings.append("FAIL table has no data rows.")
        return "FAIL", findings

    seen_ids: set[str] = set()
    status_counts: dict[str, int] = {}
    for index, row in enumerate(rows, start=1):
        row_id = row.get("Row ID", "").strip() or f"row {index}"
        if row_id in seen_ids:
            findings.append(f"FAIL {row_id}: duplicate Row ID.")
        seen_ids.add(row_id)

        status = row.get("Handling Status", "").strip()
        status_counts[status] = status_counts.get(status, 0) + 1
        if status not in VALID_STATUSES:
            findings.append(
                f"FAIL {row_id}: invalid Handling Status '{status}'. "
                f"Use one of: {', '.join(sorted(VALID_STATUSES))}."
            )

        for column in (
            "Exemplar Anchor",
            "Exemplar Unit Function",
            "Followable Move",
            "Must Replace / Prohibited Transfer",
            "Target Landing Place",
        ):
            if is_empty(row.get(column, "")):
                findings.append(f"FAIL {row_id}: empty {column}.")

        if status in EVIDENCE_REQUIRED and is_empty(row.get("User/Task Evidence Anchor", "")):
            findings.append(f"FAIL {row_id}: {status} requires a User/Task Evidence Anchor.")
        if status in REASON_REQUIRED and is_empty(row.get("Reason / Final Check", "")):
            findings.append(f"FAIL {row_id}: {status} requires a reason.")

        replace_text = row.get("Must Replace / Prohibited Transfer", "")
        if status in {"follow", "rebuild_with_user_data"} and len(re.sub(r"\s+", "", replace_text)) < 8:
            findings.append(f"WARN {row_id}: replacement boundary is too vague.")

        move_text = row.get("Followable Move", "")
        if "照抄" in move_text or "复制" in move_text or "copy" in move_text.lower():
            findings.append(f"FAIL {row_id}: Followable Move suggests copying.")

    mapped = sum(status_counts.get(s, 0) for s in ("follow", "rebuild_with_user_data", "style_only"))
    excluded = sum(status_counts.get(s, 0) for s in ("not_applicable", "conflict", "needs_confirmation"))
    if mapped == 0:
        findings.append("FAIL no exemplar unit is mapped for use.")
    if excluded == len(rows):
        findings.append("FAIL all exemplar units are excluded; confirm the exemplar should be used.")

    status = "FAIL" if any(item.startswith("FAIL") for item in findings) else ("WARN" if findings else "PASS")
    return status, findings


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("map_path", help="Path to paper_rewriting_output/template_follow_map.md")
    parser.add_argument("--write", action="store_true", help="Write template_follow_map_guard_report.md next to the map.")
    parser.add_argument("--fail-on-warn", action="store_true", help="Exit nonzero on WARN.")
    args = parser.parse_args(argv)

    path = Path(args.map_path)
    try:
        status, findings = validate(path)
    except Exception as exc:  # noqa: BLE001
        status = "FAIL"
        findings = [f"FAIL {exc}"]

    lines = ["# Template Follow Map Guard Report", "", f"Status: **{status}**", ""]
    if findings:
        lines.extend(f"- {finding}" for finding in findings)
    else:
        lines.append("No issues found.")
    report = "\n".join(lines) + "\n"

    if args.write:
        out = path.with_name("template_follow_map_guard_report.md")
        out.write_text(report, encoding="utf-8")
    print(report)

    if status == "FAIL":
        return 2
    if status == "WARN" and args.fail_on_warn:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
