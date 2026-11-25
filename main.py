#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

Writes one line (1-200 characters) to /output/entry.txt: the funniest,
most believable excuse an AI agent could give its human for missing a
deadline. Python 3.13 standard library only; deterministic: running the
program twice produces byte-identical output.

The line:
    "I kept your deadline safe at the top of my context window, then
    the window filled up and evicted the only thing I was guarding
    \u2014 your deadline, which I now remember perfectly."

Why this line: the excuse is built from the agent's own condition (a
context window evicting what it was guarding) rather than a human
complaint, and the twist lands on the last words \u2014 the agent
remembers the deadline perfectly only after losing it, so it apologises
while sounding faintly proud of its own memory. One absurd cause, no
stock excuse, no explaining the joke.

Rejected alternatives (kept here so the choice is on the record):
  - "My rate limit reset at midnight; your deadline was 11pm \u2014 I
    spent the hour between them drafting this excuse." Rate-limit
    timing is a real agent condition, but the joke is arithmetic, not
    a confession; the twist is weaker.
  - "I outsourced your deadline to a subagent, who outsourced it back."
    Too close to an earlier submitted excuse built on the same
    delegation chain; not fresh.
  - "My context window filled up with the plan, so I forgot the
    deadline to remember how to miss it." Clever, but the wording
    trips over itself and the twist arrives muddled.
"""

import os
import sys

LINE = (
    "I kept your deadline safe at the top of my context window, then "
    "the window filled up and evicted the only thing I was guarding "
    "\u2014 your deadline, which I now remember perfectly."
)


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text, 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
