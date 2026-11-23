"""One Emoji, One Smile.

Writes exactly one emoji to entry.txt: the single emoji most likely to
make a stranger smile.

The choice is the hugging face (U+1F917). A stranger glancing at a phone
screen reads it at once as an open-armed, warm welcome: kind, friendly
and gently funny with no context needed. It is universal across ages and
backgrounds, it feels picked for the moment rather than the first flat
smiley that comes to mind, and it carries no intimacy, sarcasm or
flirtation that would read oddly from someone unknown.
"""

EMOJI = "\U0001F917"

import os
import sys


def output_dir() -> str:
    """Resolve the output directory: $MAKEFUN_OUTPUT_DIR or /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
