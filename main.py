"""The Excuse That Almost Works — entry program (pure stdlib, deterministic).

Writes the one-line excuse to /output/entry.txt.
The line is judged against the published judge brief: an excuse a gamer
texts their boss to skip work on GTA 6 launch week, at most 20 words, that
a tired manager would almost believe — a real, specific, boring workplace
detail, funny on its own terms, reading like a text sent in a hurry, on an
angle the obvious excuses miss (no dead grandmother, flat tyre or fever).
"""

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"

# A moved dental appointment: specific, boring, verifiable-sounding, and the
# punchline is its own logic — a numb employee is a useless employee. No
# mention of games anywhere; 17 words, 87 characters, hurried, no setup, no signature.
ENTRY_TEXT = "Hi, my dentist moved my root canal to this morning, I'll be numb and useless till lunch"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT_PATH, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
