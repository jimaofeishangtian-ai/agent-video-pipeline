#!/usr/bin/env python3
"""Initialize pipeline state from bundled templates without overwriting files."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


FILES = {
    "project-manifest.template.yaml": "project-manifest.yaml",
    "pipeline-state.template.json": "pipeline-state.json",
    "shot-plan.template.json": "shot-plan.json",
    "qc-report.template.md": "qc-report.md",
    "timeline-manifest.template.json": "timeline-manifest.json",
    "generation-ledger.template.json": "generation-ledger.json",
    "glossary.template.json": "glossary.json",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir")
    args = parser.parse_args()
    target = Path(args.project_dir).resolve()
    target.mkdir(parents=True, exist_ok=True)
    assets = Path(__file__).resolve().parent.parent / "assets"
    created, skipped = [], []
    for source_name, target_name in FILES.items():
        destination = target / target_name
        if destination.exists():
            skipped.append(target_name)
            continue
        shutil.copyfile(assets / source_name, destination)
        created.append(target_name)
    state_path = target / "pipeline-state.json"
    if state_path.exists() and "pipeline-state.json" in created:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["updatedAt"] = datetime.now(timezone.utc).isoformat()
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"project": str(target), "created": created, "skipped": skipped}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
