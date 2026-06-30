---
name: hydraulic-writing-router
description: Personal top-level router for water-related writing. Use when the request explicitly concerns water-conservancy, hydrology, hydraulic engineering, rivers, drainage, water resources, water environment/governance, Chinese water coursework, course reports/designs, engineering reports, or LaTeX/PDF water deliverables; Chinese triggers include 水利, 水文, 水资源, 水工, 河流, 排水, 城市内涝, 水环境, 水治理, 课程报告, 课程设计, 工程报告. Also use when the user asks to coordinate PaperSpine and Nature for water-related writing. Do not use for generic non-water academic writing unless the materials contain a water/hydraulic object.
---

# Hydraulic Writing Router

Personal entrypoint for water-related papers, reports, coursework, and
LaTeX/PDF-first deliverables. It decides ownership first, then loads only the
downstream skill files needed for the task. It is a division-of-labor layer over
PaperSpine and Nature, not a fork of them: do not override their original intent
or patch their core skill files just to enforce a local preference.

## Live-Read Rule

When invoked, read this active `SKILL.md` from disk first. Do not work from
memory, old chat, backups, or archived copies.

Load downstream files only as needed:

- `paper-spine/SKILL.md`: sources, task books, templates, structure, calculations, tables, references, report repair, full/medium workflow, or final writing deliverables. Content-stage report drafts may be written and reviewed in Markdown for speed; final delivery source is assembled in LaTeX. PaperSpine keeps `final_paper/main.tex` as the final source artifact; PDF is default when compilable.
- `nature-writing/SKILL.md`: drafting or rebuilding sections from confirmed materials and chapter duties. For Chinese water course reports, course designs, engineering reports, and full report builds, load it after PaperSpine has closed source roles, chapter duties, calculation boundaries, and required tables; Nature writing owns the report body prose.
- `nature-polishing/SKILL.md`, then its `manifest.yaml` and `always_load`: polish, paragraph logic, Chinese report voice, expression density, or anti-AI regularity. For full water reports, run it after Nature writing and before final LaTeX/PDF assembly unless the user explicitly asks for a mechanical formatting-only task.
- `nature-polishing/static/core/hydraulic-engineering.md`: water-domain guardrail for drafting, polishing, and audit. Load it when the task needs object/scale checks, formula chains, parameter basis, scenario boundaries, table/figure evidence, engineering judgment, or Chinese hydraulic-report voice. This file is installed as an on-demand resource; do not rely on Nature `always_load` to bring it in.
- `paper-spine-latex/SKILL.md`: final LaTeX project assembly, source-format requirements, template integration, figure/table/equation/citation placement, compile checks, and PDF output. For water reports, use only its LaTeX/PDF rules and ignore optional conversion-to-other-format instructions.

## Output Contract

Default water-writing deliverables keep LaTeX as the final source and compile PDF
when a TeX engine is available. This is an output-stage preference layered on the
original workflow, not a replacement for it; it reduces formatting drift and
avoids a fragile final conversion step.

- Final artifacts live under `paper_rewriting_output/`: source
  `final_paper/main.tex`, compiled `final_paper/paper.pdf` when a TeX engine
  exists. Use this short form consistently; it always means the path above.
- Content source of truth: after the user confirms content, save the confirmed
  Markdown as `confirmed_content.md`. Final LaTeX assembly must build from this
  file.
- Content review: inspect Markdown or source text directly. Do not run generic
  Documents rendering, LibreOffice/soffice, or any format conversion just to
  judge whether the writing is complete or correct, and do not convert before the
  user confirms the content.
- Final assembly: build `final_paper/main.tex` from `confirmed_content.md`, use
  native `\tableofcontents`, run the LaTeX guard when available, and compile PDF
  when a TeX engine exists. Reuse existing PaperSpine/Nature LaTeX rules before
  adding local ones.
- Cover: a cover is a real asset. Defer integration until final formatting and
  ask the user for the exact cover image/PDF/template path; never hand-imitate a
  cover or TOC from memory.
- Tables: default to 三线表 (top, header, and bottom rules only; no vertical
  rules) for Chinese water reports unless the 格式要求 says otherwise. A Markdown
  content draft may use pipe tables, but final assembly must render them as
  三线表 and verify it in the PDF.

Ownership is unchanged by this preference: PaperSpine owns source mapping,
chapter duties, audits, calculations, template constraints, and final artifact
verification; Nature writing and Nature polishing own the report body prose after
the content boundary is stable, and that Nature content pass is required before
final assembly unless the task is explicitly mechanical.

## School Deliverable Mode

This is the primary use case: Chinese university 课程设计 (course design),
毕业设计 (graduation design), and 毕业论文/课程论文 (thesis/course paper). The
teacher usually supplies a fixed four-piece set — 任务书 (task book), 指导书
(guidance book), 格式要求 (format spec), and 成果封面 (cover). Route the whole
set through PaperSpine source mapping first, classify each piece, then divide
labor by deliverable track. Do not start writing before the set is classified.

### Input Classification (four-piece set)

Classify every supplied file before any writing; do not collapse them into one
bucket. This is the school-specific instance of the general source classification
in Boundary Rules: each piece has different binding force and is consumed at a
different stage.

- 任务书 / task book — binding scope + data. Defines objectives, the required
  deliverable list (成果清单), design parameters, and original data (设计流量,
  特征水位, 工程规模, 水文/地质条件). PaperSpine owns it as the strongest data and
  scope source. Its 成果清单 becomes the final completion checklist.
- 指导书 / guidance book — binding structure + method. Defines chapter order,
  calculation steps, and which methods/codes (规范) to apply. PaperSpine owns it
  as structure and method authority; it outranks generic Nature structure.
- 格式要求 / format spec — output contract only. Fonts, 字号, 行距, 页边距,
  heading numbering, 图表编号, reference style. Record during content work; apply
  only at final LaTeX/PDF assembly. Never infer the output route from it alone.
- 成果封面 / cover — real asset. Defer to final assembly; ask for the exact
  image/PDF/template path. Never hand-imitate from memory.

Anything else (师兄样本, 同组报告, 范例) is a structure-only exemplar or reference
source: it may teach chapter order and formatting habit, but must not supply
final data, formulas, parameters, wording, or conclusions.

### Template Follow Gate

When a strong exemplar is supplied (师兄样本, 同组报告, 优秀模板, 范例,
winning report, or model answer), create
`paper_rewriting_output/template_follow_map.md` before drafting body prose. This
gate prevents superficial template use: every usable exemplar paragraph, table,
formula block, caption, method step, result claim, comparison move, limitation,
or conclusion rhythm needs a handling row.

Use the task book and guidance book as hard constraints; use the exemplar as a
unit-by-unit structure guide. The final text may follow the exemplar's writing
move, order, table shape, formula placement, and evidence-to-judgment rhythm,
but it must replace the exemplar's project object, data, parameters, formula
basis, results, conclusions, recommendations, and distinctive wording with the
user's own requirement/evidence sources.

Required table:

```markdown
| Row ID | Exemplar Anchor | Exemplar Unit Function | Followable Move | Must Replace / Prohibited Transfer | User/Task Evidence Anchor | Target Landing Place | Handling Status | Reason / Final Check |
|---|---|---|---|---|---|---|---|---|
| T1 | sample.docx §1 第1段 | Opens from broad context to assigned object. | Keep the context-to-object narrowing sequence. | Replace project name, background facts, and conclusion wording. | 任务书 P.1 题目；本人资料 §背景 | draft §1 第1段 | follow | Final paragraph names the user's object and does not reuse sample wording. |
| T2 | sample.docx 表2 | Summarizes input data before calculation. | Keep table role, field order, and placement before method. | Replace all values, units, group labels, and footnotes unless supported by task data. | 分组表 Sheet1 rows 3-8 | 表2-1 | rebuild_with_user_data | Read back numbers against user data. |
```

Allowed statuses: `follow`, `rebuild_with_user_data`, `style_only`,
`not_applicable`, `conflict`, `needs_confirmation`.

- `follow` and `rebuild_with_user_data` require a user/task evidence anchor.
- `not_applicable`, `conflict`, and `needs_confirmation` require a reason.
- Do not collapse a whole exemplar section into one row when it contains
  different functions.
- Do not skip an exemplar unit silently. If it cannot be used, record why.
- After creating the map, run
  `scripts/template_follow_map_guard.py`. After drafting, run the base
  PaperSpine `template_leak_guard.py` when both exemplar and final text are
  available.

### Two Tracks

Split by deliverable type; the PaperSpine:Nature balance differs.

Design track (课程设计 / 毕业设计) — calculation-dominant. This is the priority
track.

- PaperSpine owns the large share: lock 设计依据 + 原始数据 from the 任务书, lock
  章节序 + 计算步骤 from the 指导书, then run/audit 设计计算 (调洪演算, 水力计算,
  稳定/强度校核, 工程量, 配筋) with the `公式 → 代入 → 结果 → 判断` chain visible,
  plus all 表格 and the 图纸 list.
- Nature writing owns the smaller share: 设计说明书 body prose, 摘要, 结论 —
  drafted only after calculations and chapter duties are closed.
- Nature polishing: Chinese coursework voice and anti-AI regularity, after
  content is stable.
- Hydraulic core: load it as the audit method (object/scale, datum, formula-chain,
  evidence and consistency checks, Chinese voice). It supplies the checklist, not
  the values — every datum (高程基准), 工程等别/建筑物级别, 设计/校核洪水标准, 规范,
  parameter, and formula comes from the 任务书/指导书/资料, never from a built-in
  default.
- Calculation depth: attempt the object's minimum calculation chain, e.g. for
  护岸 `水力(流速/水深) → 冲刷深度 → 护脚埋深 → 边坡稳定 → 反滤 → 工程量`. When a
  design-driving value is missing from the materials, do not defer the whole
  chain — compute with a labelled assumption (assumed value + basis such as a
  规范 typical value or 工程类比 + teacher-confirmation flag) and defer only the
  specific unresolved item.
- Scheme comparison: when the 任务书 names an economic dimension, the 比选 must
  carry at least order-of-magnitude 工程量/造价 per scheme, not adjectives alone.

Paper track (毕业论文 / 课程论文) — prose + evidence dominant.

- Nature writing owns a larger share: 引言, 讨论, 机理叙述, plus 摘要/结论.
- PaperSpine owns data, calculations, structure, and citation planning; pull
  nature-citation for 引言/讨论 references.
- Nature polishing and hydraulic-core rules apply the same way.

### Staged Handoff (design track)

1. Intake — classify the four-piece set; PaperSpine source mapping; extract the
   任务书 成果清单.
2. Lock — PaperSpine fixes 设计依据/数据 (任务书), 章节序/计算步骤 (指导书),
   calculation boundaries, table list, and 图纸 list.
3. Compute — load the hydraulic core audit checklist first (it will not
   auto-load), then PaperSpine runs/audits the minimum 设计计算 chain; keep calc
   chains and units auditable; recompute conclusion-bearing numbers; fill missing
   design-driving values with labelled assumptions rather than deferring the
   whole chain.
4. Draft — Nature writing drafts the 设计说明书 body section by section from the
   locked boundary.
5. Polish — Nature polishing for coursework voice and anti-AI regularity.
6. Confirm — after the user confirms content, save `confirmed_content.md`.
7. Assemble — PaperSpine-latex builds `final_paper/main.tex` from
   `confirmed_content.md`, applies the 格式要求 contract, integrates the real 封面
   asset, uses native `\tableofcontents`, and compiles PDF when a TeX engine
   exists.
8. Gate — check the final output against the 任务书 成果清单 before reporting done.

### 图纸 / CAD deliverables

设计类 tasks almost always require 图纸 (平面布置, 剖面, 配筋). These are normally
produced outside the text workflow (CAD), not generated as prose. Register every
required drawing in the 成果清单, reference it from the 设计说明书 by number, and
flag any drawing the text route cannot produce so the user supplies it. Do not
silently drop drawing deliverables.

## Routing Table

| Request signal | Owner | Rule |
|---|---|---|
| One sentence, one paragraph, narrow wording | Nature polishing | Use hydraulic core if water-related; verify affected facts only. |
| Draft or rebuild a section | Nature writing | Use only after object, evidence, and section duty are clear. |
| Section polish with stable structure | PaperSpine light check -> Nature polishing | Confirm duty/data boundary first, then polish. |
| Calculation, table, parameter, template, reference, LaTeX/PDF, figure/CAD issue | PaperSpine report repair | Do not smooth prose before the defect is closed. |
| Full report/paper/course design, many sections, structure rebuild, deliverable package | PaperSpine workflow + Nature content ownership | PaperSpine closes sources, calculations, template constraints, and artifact verification; Nature writing drafts/rebuilds body prose and Nature polishing finalizes paragraph logic and Chinese report voice before delivery. |
| 课程设计 / 毕业设计 / 毕业论文 with teacher 任务书·指导书·格式要求·封面 | School Deliverable Mode | Classify the four-piece set, pick the design or paper track, follow the staged handoff, and close the 任务书 成果清单 gate. |

## Boundary Rules

- PaperSpine owns workflow, source mapping, task-book/template constraints, chapter duties, calculation/table closure, citation/evidence planning, report repair, full builds, the final LaTeX source artifact, and artifact verification. It does not own the final body prose once the content boundary is stable.
- Nature writing owns prose drafting or rebuilding after materials, calculation boundaries, and chapter duties are confirmed. In full Chinese water course reports, course designs, and engineering reports, Nature writing must draft or rebuild the body sections rather than leaving body prose to PaperSpine or ad hoc script text.
- Nature polishing owns paragraph logic, clarity, rhythm, expression density, and natural Chinese coursework voice after content is stable. In full water reports, this polish pass runs before final LaTeX/PDF assembly unless the user explicitly asks for formatting only.
- Hydraulic core owns object/scale, data source, formula chain, parameter basis, scenario boundary, table/figure evidence, engineering judgment, and consistency by same object + same stage + same basis.
- Teacher instructions, task books, official templates, and user drafts outrank generic Nature style.
- Domain values are sourced, not assumed. Datum (高程基准), 工程等别/建筑物级别, 设计/校核洪水标准, applicable 规范, design parameters, and formulas must come from the 任务书, 指导书, or supplied 资料. Neither this router nor the hydraulic core injects a default standard, code, or parameter; when the materials are silent, ask the user or carry it as a labelled assumption rather than filling it from memory.
- Do not infer an output route from a template file extension alone; a supplied template still passes through content confirmation before its 格式要求 are applied at final assembly.
- When a report request includes task books, guidance files, group tables,
  official templates, and another person's report/template/sample, route to
  PaperSpine source mapping first. Classify each file as requirement source,
  user evidence source, structure-only exemplar, reference source, or
  unknown/unsafe source. For teacher-driven school tasks this is the four-piece
  set above (任务书 = requirement + data, 指导书 = requirement + structure/method,
  格式要求 = format contract, 封面 = asset). Structure-only exemplars may teach
  chapter order, calculation sequence, table/formula placement, and formatting
  habits, but they must not supply final data, formulas, parameters, wording,
  conclusions, or recommendations. When such an exemplar is supplied, close the
  Template Follow Gate before body drafting.

## Failure Modes

Treat these as defects:

- Starting work without reading the active `SKILL.md`.
- Triggering this router for generic non-water writing with no water/hydraulic object.
- Collapsing 任务书/指导书/格式要求/封面 into one undifferentiated source bucket instead of classifying the four-piece set.
- Running the prose-heavy paper track on a calculation-dominant 设计 task, or running the design track on a 论文.
- Starting writing on a 设计 task before PaperSpine has locked 任务书 data and 指导书 章节序/计算步骤.
- Delivering a 设计 task without checking the final output against the 任务书 成果清单.
- Dropping required 图纸 deliverables or failing to register them in the 成果清单.
- Letting a 师兄样本/同组报告/范例 supply final data, parameters, formulas, wording, or conclusions instead of structure only.
- Using an excellent template only for surface formatting, or skipping usable
  exemplar units without `template_follow_map.md`.
- Marking an exemplar row as `follow` while leaving its user/task evidence
  anchor empty.
- Injecting a default 规范/datum/工程等别/洪水标准/parameter/formula instead of taking it from the 任务书/指导书/资料 (or asking when the materials are silent).
- Auditing 设计计算 or hydraulic claims without first loading the hydraulic core; it does not arrive via Nature `always_load`.
- Deferring the whole 设计计算 chain (冲刷/护脚埋深/边坡稳定/工程量) instead of computing it with labelled assumptions where a value is missing.
- Comparing schemes only with adjectives when the 任务书 names an economic dimension, with no quantified 工程量/造价.
- Repeating defensive commentary about the report's own calculation depth across sections instead of stating limitations once as a boundary.
- Rendering tables as bordered/grid tables in the final report when the 格式要求 asks for 三线表.
- Running full PaperSpine for a small local wording patch.
- Treating missing calculation/source/template evidence as a polish problem.
- Skipping Nature writing/polishing on a full Chinese water course report after the calculations and chapter duties are stable.
- Letting Nature style override a course task book, teacher template, or user data.
- Treating a content-review Markdown draft as final delivery.
- Starting final LaTeX assembly before `confirmed_content.md` exists or before the user has confirmed it.
- Running format conversion repeatedly to inspect content quality, or converting before the user confirms the content.
- Delivering any full report after final assembly without `final_paper/main.tex`.
- Treating converted documents or LibreOffice output as the final report source.
- Hand-imitating a cover or TOC when an official template or real field exists, or hand-typing a TOC instead of using native `\tableofcontents`.
- Triggering generic Documents rendering, LibreOffice, or any non-LaTeX final-output tool only because a template file was present.
- Reporting completion without artifact, encoding, or calculation verification when the task edited files or numbers.

## Completion Gate

- Markdown/config: UTF-8 readback, no replacement characters.
- Content review: inspect the Markdown/source text directly and confirm chapter logic, calculations, tables, conclusions, and missing inputs before final formatting. Once confirmed, create or mark `confirmed_content.md`.
- LaTeX/PDF: after `confirmed_content.md` exists, inspect `final_paper/main.tex`, require a native `\tableofcontents` when a table of contents is needed, run the LaTeX guard when available, compile PDF when a TeX engine exists, and confirm source-format requirements from the materials are reflected or explicitly recorded as unmappable.
- PPT/Excel/PDF: inspect the actual artifact structure, not just file existence.
- 成果清单回检: for 课程设计/毕业设计, map the final deliverables back to the 任务书 成果清单 and report any missing item (设计说明书, 计算书, 图纸, 附表). Confirm the 格式要求 contract is applied or explicitly recorded as unmappable, including 三线表 rendering for report tables.
- 模板跟随门: when a structure-only exemplar is supplied,
  `template_follow_map.md` exists, passes `template_follow_map_guard.py`, and
  every usable exemplar unit is either followed, rebuilt with user data,
  style-only, not applicable, conflicting, or awaiting confirmation with a
  reason. Final text must pass a template-leak check when the exemplar and final
  text are both available.
- 计算深度门: for 设计 tasks, confirm the object's minimum calculation chain was attempted (e.g. 护岸: 水力 → 冲刷 → 护脚埋深 → 边坡稳定 → 反滤 → 工程量); each gap must be a labelled assumption or an explicit single-item deferral, never a whole-chain deferral. When the 任务书 names an economic dimension, the 比选 carries quantified 工程量/造价.
- Calculations/tables: recompute when numbers support conclusions.
- Water decisions: keep `formula -> substitution -> result -> design judgment` visible when a calculation drives the judgment.
