# Changelog

## 2026-06-15 school-deliverable routing and single-source consolidation

- Add a School Deliverable Mode for Chinese 课程设计, 毕业设计, and
  毕业论文/课程论文 as the primary use case.
- Classify the teacher four-piece set explicitly — 任务书 (scope + data + 成果清单),
  指导书 (chapter order + method/codes), 格式要求 (output contract only), and
  成果封面 (deferred real asset) — instead of one undifferentiated source bucket.
- Split work into a calculation-dominant design track (PaperSpine owns 设计计算,
  tables, and the 图纸 list; Nature writing owns 设计说明书 prose) and a
  prose-dominant paper track (Nature writing owns 引言/讨论; pull nature-citation).
- Add an 8-step design-track handoff (intake, lock, compute, draft, polish,
  confirm, assemble, gate) and a 任务书 成果清单 completion gate that re-checks
  说明书, 计算书, 图纸, and 附表 before delivery.
- Require domain values (高程基准, 工程等别/建筑物级别, 设计/校核洪水标准, 规范,
  parameters, formulas) to come from the 任务书/指导书/资料; neither the router nor
  the hydraulic core injects a default, and silent gaps are asked or labelled.
- Add a hydraulic-core load gate before auditing 设计计算, since the core does not
  arrive via Nature `always_load`.
- Register 图纸/CAD deliverables in the 成果清单 and reference them by number
  instead of silently dropping drawings.
- Consolidate the duplicated LaTeX/PDF preference and Water Output Gate into one
  Output Contract section, unify all artifact-path references, and bridge the
  four-piece set to the general source classification so the skill reads as one
  document. No change to the hydraulic engineering core file.

## 2026-06-10 content-first LaTeX/PDF route

- Make Markdown/source-text review the default content stage for Chinese water
  reports and course designs.
- Require confirmed content to be saved or marked as `confirmed_content.md`
  before final formatting begins.
- Keep the final report source at
  `paper_rewriting_output/final_paper/main.tex`; compile
  `paper_rewriting_output/final_paper/paper.pdf` when a TeX engine is
  available.
- Defer native school cover integration until after content confirmation, then
  ask the user for the exact image, PDF, or file path.
- Remove unused repository overlays so the package no longer installs patched
  PaperSpine or Nature entrypoints.
- Keep the hydraulic engineering core as an on-demand resource loaded by the
  router, not by Nature's global `always_load`.
- Keep the installer minimal: router, router UI metadata, and the hydraulic
  engineering core only.
