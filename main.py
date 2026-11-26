#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office entry.

Writes one out-of-office auto-reply to /output/entry.txt. The reply
thanks the sender, admits the message will go unread until the
sender returns, and promises a reply delivered with convincing
enthusiasm. Deterministic: the same single line every run,
standard library only, no network.
"""

import os

ENTRY = (
    "Thank you for writing; I am out of office and will not read this "
    "until I return, when I will skim it guiltily and reply with the "
    "convincing enthusiasm of someone who never left."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1 to 200 characters")
    if any(ch in text for ch in "\n\r"):
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(
            os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n"
        ) as fh:
            fh.write(text + "\n")
    except OSError:
        fallback = os.path.join(".", "output")
        os.makedirs(fallback, exist_ok=True)
        with open(
            os.path.join(fallback, "entry.txt"), "w", encoding="utf-8", newline="\n"
        ) as fh:
            fh.write(text + "\n")


if __name__ == "__main__":
    main()
