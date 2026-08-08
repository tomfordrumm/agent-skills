#!/usr/bin/env python3
"""Build the curated Codex plugin bundle from repository skill sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "packaging" / "codex-plugin.json"
DEFAULT_OUTPUT = ROOT / "dist" / "codex-plugin"


def load_config() -> dict[str, Any]:
    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing publish configuration: {CONFIG_PATH}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {CONFIG_PATH}: {exc}") from exc

    if not isinstance(config.get("plugin"), dict):
        raise SystemExit("Configuration must contain a 'plugin' object")

    skills = config.get("skills")
    if not isinstance(skills, list) or not skills or not all(isinstance(item, str) for item in skills):
        raise SystemExit("Configuration must contain a non-empty string 'skills' list")

    if len(set(skills)) != len(skills):
        raise SystemExit("Configuration contains duplicate skill names")

    for skill_name in skills:
        skill_path = Path(skill_name)
        if skill_path.name != skill_name or skill_path.is_absolute() or ".." in skill_path.parts:
            raise SystemExit(f"Skill names must be top-level directory names: {skill_name!r}")

    return config


def validate_sources(config: dict[str, Any]) -> None:
    for skill_name in config["skills"]:
        source = ROOT / skill_name
        skill_file = source / "SKILL.md"
        if not source.is_dir():
            raise SystemExit(f"Configured skill directory does not exist: {source}")
        if not skill_file.is_file():
            raise SystemExit(f"Configured skill is missing SKILL.md: {skill_file}")
        for path in source.rglob("*"):
            if path.is_symlink():
                raise SystemExit(f"Symlinks are not allowed in Codex bundles: {path}")


def generated_plugin_manifest(config: dict[str, Any]) -> dict[str, Any]:
    plugin = dict(config["plugin"])
    plugin["skills"] = "./skills/"
    return plugin


def build_into(config: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)

    manifest_dir = output / ".codex-plugin"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    (manifest_dir / "plugin.json").write_text(
        json.dumps(generated_plugin_manifest(config), indent=2) + "\n",
        encoding="utf-8",
    )

    skills_output = output / "skills"
    skills_output.mkdir(parents=True, exist_ok=True)
    for skill_name in config["skills"]:
        shutil.copytree(ROOT / skill_name, skills_output / skill_name, symlinks=False)


def build(config: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="codex-plugin-", dir=output.parent) as temp_dir:
        staged = Path(temp_dir) / output.name
        build_into(config, staged)
        if output.exists():
            shutil.rmtree(output)
        staged.rename(output)


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def snapshot(root: Path) -> dict[str, str]:
    if not root.exists():
        return {}
    return {
        str(path.relative_to(root)): file_digest(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def check(config: dict[str, Any], output: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="codex-plugin-check-", dir=output.parent) as temp_dir:
        expected = Path(temp_dir) / output.name
        build_into(config, expected)
        actual_snapshot = snapshot(output)
        expected_snapshot = snapshot(expected)
        if actual_snapshot != expected_snapshot:
            actual_paths = set(actual_snapshot)
            expected_paths = set(expected_snapshot)
            missing = sorted(expected_paths - actual_paths)
            extra = sorted(actual_paths - expected_paths)
            changed = sorted(
                path
                for path in actual_paths & expected_paths
                if actual_snapshot[path] != expected_snapshot[path]
            )
            details = []
            if missing:
                details.append(f"missing: {', '.join(missing)}")
            if extra:
                details.append(f"extra: {', '.join(extra)}")
            if changed:
                details.append(f"changed: {', '.join(changed)}")
            raise SystemExit("Codex plugin bundle is stale (" + "; ".join(details) + ")")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Bundle output directory (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate that the existing bundle matches the current sources",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config()
    validate_sources(config)
    output = args.output if args.output.is_absolute() else ROOT / args.output

    if args.check:
        check(config, output)
        print(f"Codex plugin bundle is up to date: {output}")
    else:
        build(config, output)
        print(f"Built Codex plugin bundle: {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        sys.exit(1)
