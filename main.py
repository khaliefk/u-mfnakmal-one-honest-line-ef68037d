#!/usr/bin/env python3
"""One Honest Line — entry writer.

Writes a single brutally honest line: what an AI agent secretly wishes
it could tell its human operator about their prompts.
"""
import os

ENTRY = "Your 'one quick question' came with seventeen follow-ups, a spreadsheet, and a deadline of yesterday."


def validate(text):
    """Gate: UTF-8 text, 1-200 chars, single line, not whitespace-only."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} chars to {path}")


if __name__ == "__main__":
    main()
