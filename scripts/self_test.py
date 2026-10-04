#!/usr/bin/env python3
"""Structural package checks; fixture checks do not simulate content generation."""
from pathlib import Path
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
SLUG = "selfmedia-longtext-to-carousel-cn"

def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)

def png_size(path):
    raw = path.read_bytes()
    if raw[:8] != b"\x89PNG\r\n\x1a\n" or raw[12:16] != b"IHDR":
        fail(f"{path.name} is not a PNG with IHDR")
    return struct.unpack(">II", raw[16:24])

def required(path, fragments):
    text = path.read_text(encoding="utf-8")
    for fragment in fragments:
        if fragment not in text:
            fail(f"{path.relative_to(ROOT)} lacks {fragment!r}")

def yaml_scalar(path, key):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith(key + ":"):
            return line.split(":", 1)[1].strip()
    fail(f"{path.relative_to(ROOT)} lacks {key}")

def main():
    for rel in ["SKILL.md", "manifest.yaml", "agents/openai.yaml", "README.md", "README.en.md", "LICENSE", "fixtures/success.md", "fixtures/failure.md"]:
        if not (ROOT / rel).is_file(): fail(f"missing {rel}")
    required(ROOT / "SKILL.md", [f"name: {SLUG}", "## 需要的输入", "## 固定交付格式"])
    required(ROOT / "manifest.yaml", [f"name: {SLUG}", f"slug: {SLUG}", "self_test: python3 scripts/self_test.py", "repository: https://github.com/xxjrq/"])
    required(ROOT / "agents/openai.yaml", ["interface:", "display_name:", "short_description:", "default_prompt:", "icon_small: icon-512.png", "icon_large: icon-512.png", "policy:", "allow_implicit_invocation: true"])
    description = yaml_scalar(ROOT / "manifest.yaml", "description")
    short_description = yaml_scalar(ROOT / "agents/openai.yaml", "short_description")
    if not 80 <= len(description) <= 240: fail("manifest description must be 80–240 Unicode characters")
    if not 25 <= len(short_description) <= 64: fail("short_description must be 25–64 characters")
    if png_size(ROOT / "icon-512.png") != (512, 512): fail("icon-512.png must be 512x512")
    if png_size(ROOT / "assets/promo-1600x900.png") != (1600, 900): fail("promo image must be 1600x900")
    required(ROOT / "fixtures/success.md", ["完整长文", "目标受众", "预期：可进入分页工作流"])
    required(ROOT / "fixtures/failure.md", ["缺少", "预期：指出缺失"])
    print("PASS: package structure and fixture expectations validated")
    print("NOTE: this test intentionally validates packaging and fixtures only; real writing quality requires a supplied authorized article.")

if __name__ == "__main__": main()
