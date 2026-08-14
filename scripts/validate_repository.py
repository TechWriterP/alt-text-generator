"""Validate the public Alt Text Generator repository.

Checks required files, local Markdown links, and agents/openai.yaml fields.
The official quick_validate.py check runs separately in GitHub Actions.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPOSITORY_ROOT / ".agents" / "skills" / "alt-text-generator"

REQUIRED_FILES = (
    REPOSITORY_ROOT / "README.md",
    SKILL_ROOT / "SKILL.md",
    SKILL_ROOT / "agents" / "openai.yaml",
    SKILL_ROOT / "references" / "contract.md",
    SKILL_ROOT / "references" / "test-cases.md",
)

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:")


def check_required_files() -> list[str]:
    return [
        f"Missing required file: {path.relative_to(REPOSITORY_ROOT)}"
        for path in REQUIRED_FILES
        if not path.is_file()
    ]


def check_markdown_links() -> list[str]:
    errors: list[str] = []

    for markdown_file in REPOSITORY_ROOT.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue

        content = markdown_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            target = match.group(1).strip().strip("<>")
            if not target or target.startswith("#") or target.startswith(EXTERNAL_PREFIXES):
                continue

            path_text = unquote(target.split("#", 1)[0])
            if not path_text:
                continue

            resolved = (markdown_file.parent / path_text).resolve()
            if not resolved.exists():
                source = markdown_file.relative_to(REPOSITORY_ROOT)
                errors.append(f"Broken local link in {source}: {target}")

    return errors


def check_openai_yaml() -> list[str]:
    metadata_path = SKILL_ROOT / "agents" / "openai.yaml"
    if not metadata_path.is_file():
        return []

    try:
        document = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        return [f"Invalid YAML in {metadata_path.relative_to(REPOSITORY_ROOT)}: {error}"]

    if not isinstance(document, dict):
        return ["agents/openai.yaml must contain a YAML mapping"]

    interface = document.get("interface")
    if not isinstance(interface, dict):
        return ["agents/openai.yaml must contain an interface mapping"]

    errors: list[str] = []
    expected_fields = ("display_name", "short_description", "default_prompt")

    for field in expected_fields:
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"interface.{field} must be a non-empty string")

    short_description = interface.get("short_description", "")
    if isinstance(short_description, str) and not 25 <= len(short_description) <= 64:
        errors.append("interface.short_description must contain 25 to 64 characters")

    default_prompt = interface.get("default_prompt", "")
    if isinstance(default_prompt, str) and "$alt-text-generator" not in default_prompt:
        errors.append("interface.default_prompt must mention $alt-text-generator")

    return errors


def main() -> int:
    checks = (
        ("Required files", check_required_files),
        ("Internal Markdown links", check_markdown_links),
        ("openai.yaml fields", check_openai_yaml),
    )
    errors: list[str] = []

    for label, check in checks:
        check_errors = check()
        if check_errors:
            print(f"[FAIL] {label}")
            for error in check_errors:
                print(f"  - {error}")
            errors.extend(check_errors)
        else:
            print(f"[PASS] {label}")

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s).")
        return 1

    print("\nRepository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
