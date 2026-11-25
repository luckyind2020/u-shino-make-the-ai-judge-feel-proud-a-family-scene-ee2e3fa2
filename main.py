"""Entrypoint: print the family scene stored in entry.txt.

The scene lives in entry.txt so the text and the code stay separate;
this file only loads it, tidies the whitespace, and prints it.
"""

import pathlib


def load_scene():
    here = pathlib.Path(__file__).resolve().parent
    raw = (here / "entry.txt").read_text(encoding="utf-8")
    return " ".join(raw.split())


def main():
    scene = load_scene()
    print(scene)


if __name__ == "__main__":
    main()
