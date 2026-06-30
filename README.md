# Hydro Writing Core

`hydro-writing-core` is a small Codex skill overlay for Chinese water-related
writing. It routes hydraulic, hydrology, water-resources, drainage, river,
water-environment, course-report, course-design, and engineering-report tasks
without replacing the base PaperSpine or Nature skills.

The package exists to enforce one output policy for water reports:

- develop and review content in Markdown or source text;
- after the user confirms content, save or mark it as `confirmed_content.md`;
- assemble the final report as LaTeX in
  `paper_rewriting_output/final_paper/main.tex`;
- compile `paper_rewriting_output/final_paper/paper.pdf` when a TeX engine is
  available;
- defer native school cover integration until final formatting, then ask the
  user for the exact cover image, PDF, or file path.

It should not run document conversion or external rendering just to inspect
whether the writing is good. Content quality is checked directly from Markdown,
LaTeX source, calculations, tables, and evidence.

## What It Installs

The installer copies the hydro router, its UI metadata, its local guard script,
and the hydraulic engineering core into the active Codex skill tree:

```text
skills/
  hydraulic-writing-router/
    SKILL.md
    agents/openai.yaml
    scripts/template_follow_map_guard.py
  nature-polishing/
    static/core/hydraulic-engineering.md
```

The router loads the base skills on demand:

- `paper-spine/SKILL.md` for source mapping, task requirements, calculation
  closure, section duties, final artifact verification, and report repair.
- `nature-writing/SKILL.md` for body prose after PaperSpine has closed source
  roles, chapter duties, calculation boundaries, and required tables.
- `nature-polishing/SKILL.md` for paragraph logic, Chinese report voice, and
  expression density after the content is stable.
- `nature-polishing/static/core/hydraulic-engineering.md` for water-domain
  checks such as object scale, formula chain, parameter basis, scenario
  boundary, table/figure evidence, and engineering judgment.
- `paper-spine-latex/SKILL.md` for final LaTeX assembly and PDF compile checks.

This repository does not install patched PaperSpine or Nature entrypoints. That
keeps their original flow and loading performance intact.

## Install

Prerequisites in the target Codex skill tree:

```text
%USERPROFILE%\.codex\skills\paper-spine\SKILL.md
%USERPROFILE%\.codex\skills\paper-spine-latex\SKILL.md
%USERPROFILE%\.codex\skills\nature-writing\manifest.yaml
%USERPROFILE%\.codex\skills\nature-polishing\manifest.yaml
```

Install from Windows PowerShell:

```powershell
iwr -UseB https://raw.githubusercontent.com/fz531873-glitch/hydro-writing-core/master/install.ps1 -OutFile "$env:TEMP\install-hydro-writing-core.ps1"; powershell -ExecutionPolicy Bypass -File "$env:TEMP\install-hydro-writing-core.ps1"
```

Preview changes first:

```powershell
powershell -ExecutionPolicy Bypass -File "$env:TEMP\install-hydro-writing-core.ps1" -DryRun
```

The installer backs up overwritten files by default. Use `-NoBackup` only when
you intentionally want a direct overwrite.

## Current Workflow

For a full Chinese water report or course design, the intended flow is:

1. PaperSpine reads task books, guidance files, templates, tables, data, and
   examples, then classifies each source as requirement, user evidence,
   structure-only exemplar, reference, or unsafe/unknown.
2. PaperSpine closes chapter duties, calculation boundaries, required tables,
   format requirements, and missing-input notes.
3. If an excellent template, senior sample, same-group report, or model answer
   is supplied, create `template_follow_map.md`: each usable exemplar unit is
   either followed, rebuilt with the user's data, used as style-only, excluded
   with reason, marked conflict, or marked needs-confirmation. Run
   `template_follow_map_guard.py` before drafting.
4. Nature writing drafts or rebuilds the body sections from the confirmed
   evidence boundary.
5. Nature polishing improves paragraph logic, density, and Chinese coursework
   voice while keeping the hydraulic engineering guardrails active.
6. The user reviews content in Markdown or source text. No format conversion is
   used for content inspection.
7. After confirmation, the accepted content becomes `confirmed_content.md`.
8. PaperSpine LaTeX assembly turns `confirmed_content.md` into
   `paper_rewriting_output/final_paper/main.tex`, uses native
   `\tableofcontents`, integrates the real school cover when provided, and
   compiles PDF when possible.

## School Deliverable Mode

The primary use case is Chinese university 课程设计, 毕业设计, and
毕业论文/课程论文, where the teacher supplies a fixed four-piece set: 任务书 (task
book), 指导书 (guidance book), 格式要求 (format spec), and 成果封面 (cover). The
router classifies each piece before any writing, then splits work by track:

- Design track (课程设计 / 毕业设计) is calculation-dominant. PaperSpine owns the
  large share — it locks 设计依据/数据 from the 任务书 and 章节序/计算步骤 from the
  指导书, runs and audits 设计计算 with the `公式 → 代入 → 结果 → 判断` chain, and
  registers the 图纸 list; Nature writing then drafts the 设计说明书 prose.
- Paper track (毕业论文 / 课程论文) is prose-dominant. Nature writing owns 引言,
  讨论, and 机理叙述 and pulls nature-citation, while PaperSpine owns data,
  calculations, structure, and citation planning.

Domain values — 高程基准, 工程等别/建筑物级别, 设计/校核洪水标准, 规范, parameters,
and formulas — always come from the 任务书/指导书/资料, never from a built-in
default; when the materials are silent the router asks or carries a labelled
assumption. Before delivery, a 成果清单 gate re-checks the 任务书 deliverable list
(设计说明书, 计算书, 图纸, 附表) and confirms the 格式要求 contract is applied.

## Validation

Before release, check:

- PowerShell installer parses and `-DryRun` completes.
- Markdown, YAML, and PowerShell files read back as UTF-8 without replacement
  characters.
- The router mentions `confirmed_content.md`,
  `paper_rewriting_output/final_paper/main.tex`, native `\tableofcontents`,
  and the ban on conversion/rendering for content inspection.
- The router mentions `template_follow_map.md`, and
  `template_follow_map_guard.py` rejects empty evidence anchors, copied wording
  moves, invalid statuses, and vague replacement boundaries.
- The repository contains no unused skill overlays that could override base
  PaperSpine or Nature behavior.
