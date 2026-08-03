#!/usr/bin/env python3
"""Read-only environment diagnosis for the agent video pipeline."""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
from pathlib import Path


COMMANDS = ["git", "node", "npm", "npx", "python", "ffmpeg", "ffprobe", "codex", "claude", "openclaw"]


def version(command: str) -> dict:
    path = shutil.which(command)
    result = {"found": bool(path), "path": path, "version": None}
    if not path:
        return result
    args = [path, "--version"]
    if command in {"ffmpeg", "ffprobe"}:
        args = [path, "-version"]
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=8, check=False)
        first = (proc.stdout or proc.stderr).strip().splitlines()
        result["version"] = first[0] if first else None
    except (OSError, subprocess.SubprocessError) as exc:
        result["error"] = str(exc)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    parser.add_argument("--project", default=".", help="Target project directory")
    parser.add_argument("--check-chatcut", action="store_true", help="Read-only Codex ChatCut check when Codex is present")
    args = parser.parse_args()
    project = Path(args.project).resolve()
    usage = shutil.disk_usage(project if project.exists() else Path.cwd())
    report = {
        "os": {"system": platform.system(), "release": platform.release(), "machine": platform.machine()},
        "project": str(project),
        "projectExists": project.exists(),
        "writeAccess": os.access(project if project.exists() else project.parent, os.W_OK),
        "freeDiskBytes": usage.free,
        "commands": {name: version(name) for name in COMMANDS},
        "agentHints": {
            "codex": bool(shutil.which("codex") or os.environ.get("CODEX_HOME")),
            "claudeCode": bool(shutil.which("claude")),
            "openClaw": bool(shutil.which("openclaw")),
            "trae": bool(os.environ.get("TRAE_PROJECT_ID") or os.environ.get("TRAE_WORKSPACE")),
            "workBuddy": bool(os.environ.get("WORKBUDDY_HOME")),
        },
        "credentials": {
            "arkApiKeyConfigured": bool(os.environ.get("ARK_API_KEY")),
        },
        "projectFiles": {
            "packageJson": (project / "package.json").exists(),
            "hyperframesJson": (project / "hyperframes.json").exists(),
            "pipelineState": (project / "pipeline-state.json").exists(),
            "claudeMd": (project / "CLAUDE.md").exists(),
            "agentsMd": (project / "AGENTS.md").exists(),
        },
    }
    if args.check_chatcut:
        codex_path = shutil.which("codex")
        if not codex_path:
            report["chatcutConnector"] = {"checked": True, "available": False, "error": "codex command not found"}
        else:
            try:
                proc = subprocess.run(
                    [codex_path, "mcp", "get", "chatcut"],
                    capture_output=True,
                    text=True,
                    timeout=12,
                    check=False,
                )
                report["chatcutConnector"] = {
                    "checked": True,
                    "available": proc.returncode == 0,
                    "exitCode": proc.returncode,
                    "stdout": proc.stdout.strip(),
                    "stderr": proc.stderr.strip(),
                }
            except (OSError, subprocess.SubprocessError) as exc:
                report["chatcutConnector"] = {"checked": True, "available": False, "error": str(exc)}
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
