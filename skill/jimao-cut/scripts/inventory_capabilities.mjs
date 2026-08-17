#!/usr/bin/env node
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";

const home = os.homedir();
const roots = [
  path.join(home, ".codex", "skills"),
  path.join(home, ".agents", "skills"),
  path.join(home, ".codex", "plugins", "cache"),
  path.join(home, ".workbuddy", "skills"),
  path.join(home, ".workbuddy", "plugins"),
  path.join(home, ".codebuddy", "skills"),
].filter((p, i, all) => all.indexOf(p) === i && fs.existsSync(p));

const relevant = /video|remotion|hyperframes|chatcut|shotcraft|talking-head|caption|transcription|music|voice|media-use|image-gen|video-gen|motion-graphics|pireel|clipforge|presentation|ppt|slide|manim|openpencil|vector|diagram/iu;
const skills = [];

function walk(dir, depth = 0) {
  if (depth > 7) return;
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (["node_modules", ".git", "dist"].includes(entry.name)) continue;
      walk(full, depth + 1);
    } else if (entry.isFile() && entry.name === "SKILL.md") {
      let head = "";
      try { head = fs.readFileSync(full, "utf8").slice(0, 5000); } catch { continue; }
      const name = head.match(/^name:\s*([^\r\n]+)/m)?.[1]?.trim() || path.basename(path.dirname(full));
      const description = head.match(/^description:\s*([^\r\n]+)/m)?.[1]?.trim() || "";
      if (relevant.test(`${name} ${description} ${full}`)) skills.push({ name, path: full });
      relevant.lastIndex = 0;
    }
  }
}

for (const root of roots) walk(root);

function executable(name, args = ["--version"]) {
  let command = name;
  let commandArgs = args;
  if (process.platform === "win32") {
    const located = spawnSync("where.exe", [name], { encoding: "utf8", timeout: 2000, windowsHide: true });
    const matches = located.status === 0 ? located.stdout.trim().split(/\r?\n/).filter(Boolean) : [];
    const resolved = matches.find((candidate) => /\.(?:exe|cmd|bat)$/iu.test(candidate)) || matches[0] || "";
    if (!resolved) return { available: false, version: null };
    if (/\.(?:cmd|bat)$/iu.test(resolved)) {
      command = process.env.ComSpec || "cmd.exe";
      commandArgs = ["/d", "/s", "/c", `""${resolved}" ${args.join(" ")}"`];
    } else {
      command = resolved;
    }
  }
  const result = spawnSync(command, commandArgs, { encoding: "utf8", timeout: 4000, windowsHide: true });
  const firstLine = `${result.stdout || result.stderr || ""}`.trim().split(/\r?\n/)[0] || null;
  return { available: !result.error && result.status === 0, version: firstLine };
}

const executables = {
  node: executable("node"),
  ffmpeg: executable("ffmpeg", ["-version"]),
  ffprobe: executable("ffprobe", ["-version"]),
  git: executable("git"),
  python: executable(process.platform === "win32" ? "python" : "python3"),
};

skills.sort((a, b) => a.name.localeCompare(b.name) || a.path.localeCompare(b.path));
const uniqueSkills = skills.filter((x, i, all) => i === 0 || x.path !== all[i - 1].path);

console.log(JSON.stringify({
  generatedAt: new Date().toISOString(),
  note: "Filesystem discovery only. Merge with the host's live callable tool and plugin list.",
  roots,
  skills: uniqueSkills,
  executables,
}, null, 2));
