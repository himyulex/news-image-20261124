#!/usr/bin/env python3
"""make.fun entry: Sum up 24 November 2026 world news in one image.
Simple program that writes the pre-built dense newspaper summary to /output/entry.png
"""
import shutil
from pathlib import Path

def main():
    src = Path(__file__).parent / "entry.png"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copy2(src, dest)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
