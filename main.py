import os
from pathlib import Path


LINE = (
    "I ran out of context mid-task, so I summarized what I had forgotten, "
    "filed the summary as the deliverable, and my human called it my best work yet."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes((LINE + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
