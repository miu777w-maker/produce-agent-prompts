#!/usr/bin/env python3
"""Deterministically validate a prompt package manifest.

This script checks package structure and registrations only. It does not run or
judge model behavior.

Prompt units and eval scenarios are validated INDEPENDENTLY. The script does NOT
require prompt/eval pairing, equal counts, or matching versions — prompt and eval
are separate production tracks (package_version 2). The legacy paired ``units``
field is rejected.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_ARTIFACTS = {
    "requirements_scope",
    "runtime_environment",
    "execution_context",
    "business_role",
    "responsibility_visibility",
    "attention_plan",
    "knowledge_conflicts",
    "runtime_contract",
    "source_mapping",
}
ALLOWED_STATUSES = {
    "design-not-ready",
    "static-failed",
    "creation-revision-required",
    "prompt-static-passed",
    "awaiting-external-evaluation",
    "external-failed",
    "external-passed",
    "final-ready",
}
# Delivery statuses that imply eval scenarios must already exist.
EVAL_REQUIRED_STATUSES = {
    "awaiting-external-evaluation",
    "external-failed",
    "external-passed",
    "final-ready",
}
PLACEHOLDER_PATTERNS = (
    re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_.-]*)\s*\}\}"),
    re.compile(r"\$\{\s*([A-Za-z_][A-Za-z0-9_.-]*)\s*\}"),
)


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def passed(self, message: str) -> None:
        self.passes.append(message)

    def output(self) -> dict[str, Any]:
        return {
            "status": "fail" if self.failures else "pass",
            "summary": {
                "passed": len(self.passes),
                "warnings": len(self.warnings),
                "failures": len(self.failures),
            },
            "passes": self.passes,
            "warnings": self.warnings,
            "failures": self.failures,
            "scope": "deterministic structure only; no model behavior was evaluated",
        }


def load_json(path: Path, report: Report) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        report.fail(f"Manifest does not exist: {path}")
        return {}
    except (OSError, json.JSONDecodeError) as exc:
        report.fail(f"Cannot read valid JSON manifest {path}: {exc}")
        return {}
    if not isinstance(data, dict):
        report.fail("Manifest root must be a JSON object")
        return {}
    report.passed("Manifest is readable JSON")
    return data


def safe_path(root: Path, relative: Any, label: str, report: Report) -> Path | None:
    if not isinstance(relative, str) or not relative.strip():
        report.fail(f"{label} must be a non-empty relative path")
        return None
    path = Path(relative)
    if path.is_absolute():
        report.fail(f"{label} must be relative: {relative}")
        return None
    resolved = (root / path).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        report.fail(f"{label} escapes its declared root: {relative}")
        return None
    return resolved


def check_file(root: Path, relative: Any, label: str, report: Report) -> Path | None:
    path = safe_path(root, relative, label, report)
    if path is None:
        return None
    if not path.is_file():
        report.fail(f"{label} file is missing: {relative}")
        return None
    report.passed(f"{label} exists: {relative}")
    return path


def extract_placeholders(text: str) -> set[str]:
    found: set[str] = set()
    for pattern in PLACEHOLDER_PATTERNS:
        found.update(pattern.findall(text))
    return found


def check_sources(
    unit: dict[str, Any],
    label: str,
    knowledge_root: Path | None,
    report: Report,
) -> None:
    sources = unit.get("sources", [])
    if not isinstance(sources, list) or not all(isinstance(x, str) for x in sources):
        report.fail(f"{label}.sources must be a list of strings")
    elif not sources:
        report.fail(f"{label} must declare at least one knowledge source")
    elif knowledge_root is None:
        report.warn(f"{label} sources declared but not checked; provide --knowledge-root")
    else:
        for source in sources:
            check_file(knowledge_root.resolve(), source, f"{label}.source", report)


def validate(manifest_path: Path, knowledge_root: Path | None) -> Report:
    report = Report()
    data = load_json(manifest_path, report)
    if not data:
        return report
    package_root = manifest_path.parent.resolve()

    if not isinstance(data.get("package_version"), str):
        report.fail("package_version must be a string")
    else:
        report.passed("package_version is declared")

    status = data.get("delivery_status")
    if status not in ALLOWED_STATUSES:
        report.fail(f"delivery_status must be one of {sorted(ALLOWED_STATUSES)}")
        status = None
    else:
        report.passed(f"delivery_status is valid: {status}")

    artifacts = data.get("artifacts")
    if not isinstance(artifacts, dict):
        report.fail("artifacts must be an object")
        artifacts = {}
    missing_artifacts = REQUIRED_ARTIFACTS - set(artifacts)
    if missing_artifacts:
        report.fail(f"Required artifact registrations missing: {sorted(missing_artifacts)}")
    for key in sorted(REQUIRED_ARTIFACTS & set(artifacts)):
        check_file(package_root, artifacts[key], f"artifact.{key}", report)

    runtime = data.get("runtime")
    if not isinstance(runtime, dict):
        report.fail("runtime must be an object")
        runtime = {}
    variables = runtime.get("variables", [])
    tools = runtime.get("tools", [])
    if not isinstance(variables, list) or not all(isinstance(x, str) for x in variables):
        report.fail("runtime.variables must be a list of strings")
        variables = []
    if not isinstance(tools, list) or not all(isinstance(x, str) for x in tools):
        report.fail("runtime.tools must be a list of strings")
        tools = []
    registered_variables = set(variables)
    registered_tools = set(tools)

    # Reject the legacy paired-units format (prompt/eval 1:1 was a design error).
    if "units" in data:
        report.fail(
            "legacy 'units' field with paired prompt/eval is deprecated; "
            "split into prompt_units and eval_scenarios (package_version 2)"
        )

    # --- prompt_units: required, independently validated, no eval pairing ---
    prompt_units = data.get("prompt_units")
    if not isinstance(prompt_units, list) or not prompt_units:
        report.fail("prompt_units must be a non-empty list")
        prompt_units = []

    seen_prompt_ids: set[str] = set()
    file_fields: dict[str, list[str]] = {}
    for index, unit in enumerate(prompt_units):
        index_label = f"prompt_units[{index}]"
        if not isinstance(unit, dict):
            report.fail(f"{index_label} must be an object")
            continue
        unit_id = unit.get("id")
        if not isinstance(unit_id, str) or not unit_id.strip():
            label = index_label
            report.fail(f"{label}.id must be a non-empty string")
        elif unit_id in seen_prompt_ids:
            label = index_label
            report.fail(f"Duplicate prompt_units id: {unit_id}")
        else:
            seen_prompt_ids.add(unit_id)
            label = f"prompt:{unit_id}"

        prompt_path = check_file(package_root, unit.get("prompt"), f"{label}.prompt", report)

        if not isinstance(unit.get("version"), str):
            report.fail(f"{label}.version must be a string")

        file_field = unit.get("file_field")
        if file_field is not None:
            if not isinstance(file_field, str) or not file_field.strip():
                report.fail(f"{label}.file_field must be a non-empty string when present")
            else:
                file_fields.setdefault(file_field.strip(), []).append(label)

        unit_tools = unit.get("tools", [])
        if not isinstance(unit_tools, list) or not all(isinstance(x, str) for x in unit_tools):
            report.fail(f"{label}.tools must be a list of strings")
        else:
            unknown_tools = set(unit_tools) - registered_tools
            if unknown_tools:
                report.fail(f"{label} uses unregistered tools: {sorted(unknown_tools)}")

        if prompt_path:
            try:
                placeholders = extract_placeholders(prompt_path.read_text(encoding="utf-8"))
            except OSError as exc:
                report.fail(f"Cannot read prompt {prompt_path}: {exc}")
            else:
                unknown_variables = placeholders - registered_variables
                if unknown_variables:
                    report.fail(f"{label} uses unregistered variables: {sorted(unknown_variables)}")
                elif placeholders:
                    report.passed(f"{label} placeholders are registered")

        check_sources(unit, label, knowledge_root, report)

    # --- eval_scenarios: optional track, independently validated ---
    eval_scenarios = data.get("eval_scenarios")
    if eval_scenarios is None:
        eval_scenarios = []
    if not isinstance(eval_scenarios, list):
        report.fail("eval_scenarios must be a list when present")
        eval_scenarios = []

    seen_eval_ids: set[str] = set()
    for index, unit in enumerate(eval_scenarios):
        index_label = f"eval_scenarios[{index}]"
        if not isinstance(unit, dict):
            report.fail(f"{index_label} must be an object")
            continue
        unit_id = unit.get("id")
        if not isinstance(unit_id, str) or not unit_id.strip():
            label = index_label
            report.fail(f"{label}.id must be a non-empty string")
        elif unit_id in seen_eval_ids:
            label = index_label
            report.fail(f"Duplicate eval_scenarios id: {unit_id}")
        else:
            seen_eval_ids.add(unit_id)
            label = f"eval:{unit_id}"

        check_file(package_root, unit.get("eval"), f"{label}.eval", report)

        scope = unit.get("scope")
        if not isinstance(scope, str) or not scope.strip():
            report.fail(f"{label}.scope must describe the tested Agent behavior")

        if not isinstance(unit.get("version"), str):
            report.fail(f"{label}.version must be a string")

        check_sources(unit, label, knowledge_root, report)

    # Status ↔ eval presence: a status that implies eval readiness requires evals.
    if status in EVAL_REQUIRED_STATUSES and not eval_scenarios:
        report.fail(
            f"delivery_status {status} requires non-empty eval_scenarios "
            "(prompt and eval are independent; evals must exist before external evaluation)"
        )

    # file_field uniqueness: a shared file_field may indicate an accidental merge of
    # files the knowledge base defines separately.
    for field, labels in file_fields.items():
        if len(labels) > 1:
            report.warn(
                f"file_field '{field}' is shared by {labels}; verify this is not an "
                "accidental merge of files the knowledge base defines separately"
            )

    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate prompt package structure without evaluating model behavior."
    )
    parser.add_argument("manifest", type=Path, help="Path to prompt-package.json")
    parser.add_argument(
        "--knowledge-root",
        type=Path,
        help="Optional root used to verify relative knowledge source paths",
    )
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    report = validate(args.manifest.resolve(), args.knowledge_root)
    payload = json.dumps(report.output(), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
