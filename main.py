#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The 3 AM Excuse": The wallet speaks from its own evidence (thumbprint, PIN attempts, destination) and its own grudge, the joke exists only at 3 AM, and it avoids the brief's banned battery/firmware/cold-storage stock angles, ending on the getaway-car turn.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Signing refused: at 3 AM your thumbprint arrives with a yawn, three wrong PINs and an ex's address - I am not your getaway car."
TEXT = LINE + "\n"
MAX_CHARS = 200
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
