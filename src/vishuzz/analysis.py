"""Core text analysis utilities for vishuzz."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TextSummary:
    """Represents a concise summary of a text body."""

    characters: int
    words: int
    lines: int
    unique_words: int



def summarize_text(content: str) -> TextSummary:
    """Compute basic statistics from text content.

    Args:
        content: The text to analyze.

    Returns:
        A TextSummary with character, word, line, and unique-word counts.
    """
    normalized = content.strip()
    words = [word for word in normalized.split() if word]
    unique_words = {word.lower() for word in words}

    lines = 0 if not normalized else len(normalized.splitlines())

    return TextSummary(
        characters=len(content),
        words=len(words),
        lines=lines,
        unique_words=len(unique_words),
    )



def summarize_file(path: Path) -> TextSummary:
    """Read a text file and summarize its contents."""
    return summarize_text(path.read_text(encoding="utf-8"))
