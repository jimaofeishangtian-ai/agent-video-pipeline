#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const file = process.argv[2];
if (!file) {
  console.error("Usage: node validate_edit_plan.mjs <edit-plan.json>");
  process.exit(2);
}

const errors = [];
const warnings = [];
let plan;
try {
  plan = JSON.parse(fs.readFileSync(path.resolve(file), "utf8"));
} catch (error) {
  console.error(`Invalid JSON or unreadable file: ${error.message}`);
  process.exit(2);
}

function required(value, label) {
  if (value === undefined || value === null || value === "") errors.push(`${label} is required`);
}

required(plan.schemaVersion, "schemaVersion");
required(plan.project?.id, "project.id");
required(plan.project?.status, "project.status");
required(plan.ownership?.timelineOwner, "ownership.timelineOwner");
required(plan.ownership?.renderOwner, "ownership.renderOwner");
required(plan.brief?.purpose, "brief.purpose");
required(plan.brief?.aspectRatio, "brief.aspectRatio");
required(plan.brief?.fps, "brief.fps");
required(plan.brief?.language, "brief.language");

const sourceModes = new Set(["talking-head", "footage", "script", "deck", "mixed"]);
if (plan.brief?.sourceMode !== undefined && !sourceModes.has(plan.brief.sourceMode)) errors.push("brief.sourceMode is invalid");
const adaptationLevels = new Set(["reinterpret", "balanced", "faithful"]);
if (plan.brief?.adaptationLevel !== undefined && !adaptationLevels.has(plan.brief.adaptationLevel)) errors.push("brief.adaptationLevel is invalid");
const narrationSources = new Set(["source-audio", "user-recording", "authorized-recording", "tts", "authorized-clone", "silent-prototype"]);
if (plan.narration?.source !== undefined && !narrationSources.has(plan.narration.source)) errors.push("narration.source is invalid");
if (["script", "deck"].includes(plan.brief?.sourceMode) && !plan.narration?.source) warnings.push("script/deck route should record narration.source");
if (plan.narration?.source === "authorized-clone" && plan.narration?.authorization !== "user-approved") errors.push("authorized-clone requires narration.authorization=user-approved");

if (!Number.isFinite(plan.brief?.fps) || plan.brief.fps <= 0) errors.push("brief.fps must be a positive number");
if (!Array.isArray(plan.sources)) errors.push("sources must be an array");
if (!Array.isArray(plan.beats) || plan.beats.length === 0) errors.push("beats must be a non-empty array");
if (!Array.isArray(plan.tracks)) errors.push("tracks must be an array");
if (typeof plan.render?.authorized !== "boolean") errors.push("render.authorized must be boolean");
if (plan.render?.authorized && plan.review?.status !== "approved") warnings.push("render is authorized but review.status is not approved");

const purpose = new Set(["hook", "context", "claim", "step", "comparison", "evidence", "transition", "result", "cta", "breath"]);
const relation = new Set(["parallel", "sequence", "progress", "compare", "cause", "evidence", "none"]);
const role = new Set(["neutral", "tech", "success", "growth", "money", "result", "risk", "warning"]);
const visual = new Set(["face", "real-screen", "broll", "topic", "viewpoint", "number", "process", "evidence", "chart", "tool-screen", "no-effect"]);
const ids = new Set();
let previousEnd = -Infinity;

for (const [index, beat] of (plan.beats || []).entries()) {
  const at = `beats[${index}]`;
  required(beat.id, `${at}.id`);
  if (ids.has(beat.id)) errors.push(`${at}.id duplicates ${beat.id}`);
  ids.add(beat.id);
  if (!Number.isFinite(beat.startSec) || !Number.isFinite(beat.endSec) || beat.startSec < 0 || beat.endSec <= beat.startSec) {
    errors.push(`${at} must satisfy 0 <= startSec < endSec`);
  }
  if (Number.isFinite(beat.startSec) && beat.startSec < previousEnd - 0.001) warnings.push(`${at} overlaps the previous beat`);
  if (Number.isFinite(beat.endSec)) previousEnd = Math.max(previousEnd, beat.endSec);
  required(beat.spokenText, `${at}.spokenText`);
  required(beat.captionText, `${at}.captionText`);
  required(beat.summary, `${at}.summary`);
  if (!purpose.has(beat.purpose)) errors.push(`${at}.purpose is invalid`);
  if (!relation.has(beat.relation)) errors.push(`${at}.relation is invalid`);
  if (!role.has(beat.role)) errors.push(`${at}.role is invalid`);
  if (!visual.has(beat.visualType)) errors.push(`${at}.visualType is invalid`);
  if (!Array.isArray(beat.protectedRegions)) errors.push(`${at}.protectedRegions must be an array`);
  if (beat.shot?.enterSec !== undefined && (beat.shot.enterSec < beat.startSec || beat.shot.enterSec > beat.endSec)) warnings.push(`${at}.shot.enterSec is outside the beat`);
  if (beat.shot?.exitSec !== undefined && (beat.shot.exitSec < beat.startSec || beat.shot.exitSec > beat.endSec)) warnings.push(`${at}.shot.exitSec is outside the beat`);
  if (beat.visualType === "real-screen" && !beat.evidence) warnings.push(`${at} uses real-screen without evidence metadata`);
}

const result = { valid: errors.length === 0, file: path.resolve(file), errors, warnings, beatCount: plan.beats?.length || 0 };
console.log(JSON.stringify(result, null, 2));
process.exit(errors.length ? 1 : 0);
