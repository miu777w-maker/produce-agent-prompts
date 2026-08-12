# Version 0.3.0

## Readiness

- Prompt Inspection: protocol updated to seven gates and prompt/eval separation; awaiting a new whole-system regression run under v0.3.
- Prompt Creation: protocol restructured — prompt and eval production fully separated, minimal delivery + on-demand append, seven-gate closure, file-boundary/naming protocol, directed retrieval with stop protocol, confirmation points as hard gates; awaiting the first real production run under v0.3.
- Prompt Revision: protocol updated; not yet validated end to end.
- Eval Creation: newly independent track (evaluates full Agent business behavior, derives independently from the knowledge base); designed, not yet validated end to end.
- External evaluation to `final-ready`: designed, not yet validated end to end.

## V0.3 changes

- Fully separated Prompt production and Eval production into independent tracks. Clarified that knowledge-base "synchronization" means project-phase synchronization, not production binding. Removed the per-unit prompt+eval co-generation rule across `SKILL.md`, `task-protocols.md`, `workflow-and-state.md`, `validation-and-external-handoff.md`, `artifact-templates.md` and the validator.
- Added Eval Creation as an independent first-class track: the tested object is full Agent business behavior; evals derive independently from the knowledge base; scenario count is driven by business cases, not prompt count; no `eval → prompt` dependency.
- Promoted "requirements-first and scope derivation" to the first of **seven** core gates (was six). Each gate must produce concrete constraints on final files and be reverse-checked before delivery; filling a table is no longer a pass.
- Added the file-boundary and naming protocol: knowledge-base file fields default to independent physical files; no self-added prefixes or merges; an expected-vs-actual file checklist is required before delivery.
- Added the directed-retrieval and stop protocol for large knowledge bases; full-library reads are no longer the default; retrieval scope, stop reason and possible omissions are recorded.
- Confirmation points are now hard stage-transition gates, not optional communication.
- Minimal delivery + on-demand append: Prompt Creation converges on `prompts/` + `prompt-production-basis.md` + `prompt-static-check.md` (+ optional `task-state.md`); extra Markdown is generated only via an on-demand confirmation gate when a concrete consumer exists.
- Honest status: design assumptions cannot be marked `pass`; added `creation-revision-required` and `prompt-static-passed`; runtime-evidence gaps are split into blocking (business semantics) vs warning (engineering detail).
- Stage-required references are now a mandatory pre-stage checklist, not "on-demand optional".
- Validator (`package_version` 2): validates `prompt_units` and `eval_scenarios` independently; rejects the legacy paired `units` field; checks `file_field` uniqueness and status/eval-presence consistency.

## Evidence

See `development/process-history/29-v0-3-revision-checkpoint.md`. The revision is based on the first real Creation retrospective (external archive `28-v0-2-creation-retrospective-and-next-session-handoff.md`), the Creation execution handoff, the original task input, and the user's in-session rulings.
