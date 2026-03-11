from pathlib import Path

from vishuzz.analysis import TextSummary, summarize_file, summarize_text


def test_summarize_text_counts() -> None:
    sample = "Hello world\nHello there"
    result = summarize_text(sample)

    assert result == TextSummary(characters=len(sample), words=4, lines=2, unique_words=3)


def test_summarize_text_empty() -> None:
    result = summarize_text("   ")
    assert result.words == 0
    assert result.lines == 0
    assert result.unique_words == 0


def test_summarize_file(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"
    file_path.write_text("a b c\na", encoding="utf-8")

    result = summarize_file(file_path)
    assert result.words == 4
    assert result.lines == 2
    assert result.unique_words == 3
