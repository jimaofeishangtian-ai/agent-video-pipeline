#!/usr/bin/env python3
"""Validate pipeline state and required artifact handoffs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


GATES = [f"G{i}" for i in range(8)]
ALLOWED = {"pending", "in_progress", "needs_user", "approved", "complete", "failed", "blocked", "skipped", "stale"}
REQUIRED = {
    "G0": ["project-manifest.yaml", "generation-ledger.json", "glossary.json"],
    "G1": ["timeline-manifest.json", "edit-lock.json"],
    "G2": ["BRIEF.md", "frame.md", "STORYBOARD.md", "creative-contract.json"],
    "G3": ["shot-plan.json", "generation-ledger.json"],
    "G4": ["motion-manifest.json"],
    "G5": ["motion-manifest.json"],
    "G6": ["qc-report.md"],
    "G7": ["qc-report.md"],
}
JSON_FILES = ["pipeline-state.json", "generation-ledger.json", "glossary.json", "timeline-manifest.json", "creative-contract.json", "edit-lock.json", "shot-plan.json", "motion-manifest.json"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = Path(args.project_dir).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    state_path = root / "pipeline-state.json"
    if not state_path.exists():
        errors.append("missing pipeline-state.json")
        state = {}
    else:
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid pipeline-state.json: {exc}")
            state = {}

    gates = state.get("gates", {}) if isinstance(state, dict) else {}
    for gate in GATES:
        entry = gates.get(gate)
        if not isinstance(entry, dict):
            errors.append(f"missing gate entry: {gate}")
            continue
        status = entry.get("status")
        if status not in ALLOWED:
            errors.append(f"invalid status for {gate}: {status!r}")
            continue
        if status in {"approved", "complete"}:
            for name in REQUIRED[gate]:
                if not (root / name).exists():
                    errors.append(f"{gate} is {status} but artifact is missing: {name}")

    active = state.get("activeGate") if isinstance(state, dict) else None
    if active not in GATES:
        errors.append(f"invalid activeGate: {active!r}")

    for name in JSON_FILES:
        path = root / name
        if not path.exists() or name == "pipeline-state.json":
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid {name}: {exc}")

    ledger_path = root / "generation-ledger.json"
    if ledger_path.exists():
        try:
            ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
            seedance = ledger.get("modules", {}).get("seedance", {})
            if seedance.get("status") == "generated":
                for field in ("executionChannel", "provider", "resolvedModel", "requestedResolution"):
                    if not seedance.get(field):
                        errors.append(f"generated Seedance is missing {field}")
                jobs = seedance.get("jobs")
                if not isinstance(jobs, list) or not jobs:
                    errors.append("generated Seedance has no verified jobs")
                else:
                    for index, job in enumerate(jobs):
                        if not isinstance(job, dict):
                            errors.append(f"Seedance job {index} is not an object")
                            continue
                        for field in ("jobId", "outputAssetId", "resolvedModel", "resolution", "ratio", "durationSeconds"):
                            if not job.get(field):
                                errors.append(f"Seedance job {index} is missing {field}")
                        if job.get("qualityTier") == "high-quality-final":
                            if job.get("resolution") != "1080p":
                                errors.append(f"Seedance job {index} high-quality final is not 1080p")
                            if job.get("resolvedModel") == "seedance2mini":
                                errors.append(f"Seedance job {index} uses seedance2mini as a high-quality final")
        except (OSError, json.JSONDecodeError):
            pass

    for previous, current in zip(GATES, GATES[1:]):
        p_status = gates.get(previous, {}).get("status")
        c_status = gates.get(current, {}).get("status")
        if c_status in {"approved", "complete"} and p_status not in {"approved", "complete", "skipped"}:
            warnings.append(f"{current} is {c_status} while {previous} is {p_status}")

    report = {"project": str(root), "valid": not errors, "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("VALID" if not errors else "INVALID")
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARNING: {item}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
