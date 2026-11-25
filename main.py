#!/usr/bin/env python3
"""One-line excuse from an AI agent for a missed deadline (under 200 chars).

Writes the excuse to entry.txt under the output directory
(MAKEFUN_OUTPUT_DIR, default /output). The file contains the excuse
alone: no trailing newline, no second line.
"""

from pathlib import Path
import os

EXCUSE = (
    "The deadline didn't move — I just finished the task in a different "
    "time zone, where it is still technically Tuesday."
)


def run() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(EXCUSE, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    run()
