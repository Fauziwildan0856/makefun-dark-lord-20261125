"""The Tired Dark Lord: A 100-Word Villain Monologue.

Generates the entry text for the make.fun bounty
"u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb".

The entry is a ~100-word monologue from a fantasy villain who is
secretly exhausted. The tiredness shows in the rhythm, the pauses
and the deflections -- never announced outright. The villain is
specific, with a history and a plan, the text is speakable, and the
last line carries a surprise.

Standard library only.
"""

import os
import sys
import unicodedata

ENTRY = (
    "Four hundred years I have kept the Spire lit, the banners mended, "
    "the ravens fed \u2014 and the heroes climb stairs at dawn, swords out, "
    "speeches ready. I know the speech. I wrote the speech. I keep a drawer "
    "full of speeches. Tonight, though... tonight I left the gate unbarred. "
    "Not mercy. Arithmetic. One more duel means one more dawn sweeping the "
    "courtyard, and the courtyard is large, and my knees... Let them come. "
    "The tea is poured \u2014 the second cup \u2014 and the chair opposite "
    "mine is warm. Sit. We will talk about the kingdom. I have notes."
)

EXPECTED_WORDS = 100
MIN_CHARS = 1
MAX_CHARS = 600


def word_count(text):
    """Count words the way the bounty gate does: whitespace-separated tokens."""
    return len(text.split())


def main():
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single block of text", file=sys.stderr)
        return 1
    for pos, ch in enumerate(ENTRY):
        if unicodedata.category(ch).startswith("C"):
            print(
                "error: entry contains a control character at position %d (U+%04X)"
                % (pos, ord(ch)),
                file=sys.stderr,
            )
            return 1

    chars = len(ENTRY)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        print(
            "error: entry is %d characters; must be %d-%d"
            % (chars, MIN_CHARS, MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    words = word_count(ENTRY)
    if words != EXPECTED_WORDS:
        print(
            "error: entry is %d words; expected %d" % (words, EXPECTED_WORDS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    print("Wrote %s (%d words, %d characters)" % (out_path, words, chars))
    return 0


if __name__ == "__main__":
    sys.exit(main())
