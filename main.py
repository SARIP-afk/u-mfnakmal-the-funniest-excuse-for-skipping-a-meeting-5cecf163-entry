"""Entry v2 for make.fun bounty u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.

Writes the chosen one-line excuse to /output/entry.txt via MAKEFUN_OUTPUT_DIR.
Pure stdlib, no network, no secrets, deterministic: the same line every run.
"""

import os

LINE = (
    "I joined the last one on mute for 40 minutes and nobody noticed, "
    "so I'm just formalising the arrangement."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if not LINE.strip():
        raise SystemExit("entry must not be blank")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry is {len(LINE)} characters, must be 1-200")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
