#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFERRED_SOURCE = ROOT / "vendor" / "antigravity-kit" / ".agent" / "skills"
FALLBACK_SOURCE = ROOT / ".agent" / "skills"
DEST = ROOT / ".agents" / "skills"


def choose_source() -> Path:
    if PREFERRED_SOURCE.exists():
        return PREFERRED_SOURCE
    if FALLBACK_SOURCE.exists():
        return FALLBACK_SOURCE
    raise FileNotFoundError("No skill source found in vendor/.agent/skills or .agent/skills")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text

    # Multiline YAML frontmatter (preferred)
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.DOTALL)
    if m:
        raw = m.group(1)
        body = text[m.end() :]
    else:
        # Inline/minified fallback: --- key: value key2: value2 ---
        m2 = re.match(r"^---\s*(.*?)\s*---\s*", text, flags=re.DOTALL)
        if not m2:
            return {}, text
        raw = m2.group(1)
        body = text[m2.end() :]

    fm: dict[str, str] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fm[key.strip()] = value.strip().strip('"').strip("'")

    # Fallback parser for truly minified key: value pairs on one line
    if not fm and raw:
        for key, value in re.findall(r"([A-Za-z0-9_-]+)\s*:\s*([^:]+?)(?=\s+[A-Za-z0-9_-]+\s*:|$)", raw):
            fm[key.strip()] = value.strip().strip('"').strip("'")

    return fm, body


def normalize_frontmatter(fm: dict[str, str], skill_dir: Path) -> dict[str, str]:
    out = dict(fm)
    if "name" not in out or not out["name"]:
        out["name"] = skill_dir.name
    if "description" not in out or not out["description"]:
        out["description"] = f"Skill for {skill_dir.name}."

    if "allowed-tools" in out:
        normalized = re.sub(r"\s+", " ", out["allowed-tools"].replace(",", " ")).strip()
        out["allowed-tools"] = normalized

    return out


def to_frontmatter_text(fm: dict[str, str]) -> str:
    priority = ["name", "description", "allowed-tools"]
    keys = [k for k in priority if k in fm] + [k for k in fm if k not in priority]
    lines = ["---"]
    for key in keys:
        lines.append(f"{key}: {fm[key]}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def copy_and_convert(source: Path, dest: Path) -> int:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(source, dest)

    converted = 0
    for skill_md in dest.rglob("SKILL.md"):
        original = skill_md.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(original)
        fm = normalize_frontmatter(fm, skill_md.parent)
        rewritten = to_frontmatter_text(fm) + body.lstrip("\n")
        skill_md.write_text(rewritten, encoding="utf-8")
        converted += 1
    return converted


def main() -> None:
    source = choose_source()
    converted = copy_and_convert(source, DEST)
    print(f"Source: {source}")
    print(f"Destination: {DEST}")
    print(f"Converted SKILL.md files: {converted}")


if __name__ == "__main__":
    main()
