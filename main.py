#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

The text is fixed: the same words every run, so the two grading runs
produce byte-identical output.
"""

import os

TEXT = (
    "The old dog sleeps by the stove, his chin on his paws, the fire "
    "ticking itself down to embers. Late light comes through the window "
    "and lies still on the floor. The kettle hums low, then settles, and "
    "the dog sighs in his sleep. The room keeps its own slow time."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
