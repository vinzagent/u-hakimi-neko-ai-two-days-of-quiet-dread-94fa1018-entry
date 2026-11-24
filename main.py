"""Two Days of Quiet Dread (u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018).

One code review comment that genuinely approves the pull request while
carrying quiet existential dread: the code is clean, well tested, and
certain to outlive everyone who reviewed it — so the reviewer approves
it, then archives their own job description as legacy code, the one
concrete absurd work detail that makes the dread land.

The gate allows 1 to 140 characters, so refuse to ship anything longer,
anything blank, or anything that is not exactly one line.
"""

import os

SETUP = (
    "LGTM. Clean, well-tested, and certain to outlive every one of "
    "us — "
)
PUNCHLINE = (
    "I approved it, then archived my own job description as "
    "legacy code."
)
LINE = SETUP + PUNCHLINE

chars = len(LINE)
if chars < 1 or chars > 140:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-140 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
