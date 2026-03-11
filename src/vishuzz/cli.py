"""Command-line interface for vishuzz."""

from __future__ import annotations

import argparse
from pathlib import Path

from .analysis import summarize_file


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="vishuzz",
        description="Analyze a text file and print summary metrics.",
    )
    parser.add_argument("path", type=Path, help="Path to a UTF-8 text file")
    return parser



def main() -> None:
    """Run the CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args()

    if not args.path.exists():
        parser.error(f"File not found: {args.path}")

    summary = summarize_file(args.path)
    print(f"characters: {summary.characters}")
    print(f"words: {summary.words}")
    print(f"lines: {summary.lines}")
    print(f"unique_words: {summary.unique_words}")


if __name__ == "__main__":
    main()
