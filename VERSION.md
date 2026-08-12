# Version 0.2.0

## Readiness

- Inspection: validated through two whole-system runs; the second run verified independent inventory reconstruction, knowledge/runtime blocking, file-based reporting, and non-mutating behavior.
- Creation: protocol ready for first real knowledge-base production run; not yet validated end to end.
- Revision: designed, not yet validated end to end.
- Eval-only: designed, not yet validated end to end.
- External evaluation to `final-ready`: designed, not yet validated end to end.

## V0.2 changes

- Added `inspection-blocked` and deterministic inspection status aggregation.
- Added the Inspection view of the six core gates.
- Consolidated runtime-evidence degradation and engineering handoff rules.
- Added existing-eval audit requirements.
- Clarified that the eight-stage workflow belongs to Creation.
- Promoted independent reconstruction of the expected prompt inventory to a core Inspection rule.
- Allowed lightweight orientation before scope confirmation.
- Added overridable default output directories and separate knowledge/runtime handoff files.

## Evidence

See `development/process-history/25-second-inspection-regression-review.md` and `development/process-history/26-v0-2-release-scope-and-first-principles-audit.md`.
