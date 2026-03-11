import pytest

from vishuzz.cli import build_parser


def test_parser_has_path_argument() -> None:
    parser = build_parser()
    args = parser.parse_args(["README.md"])
    assert str(args.path).endswith("README.md")


def test_parser_requires_path() -> None:
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])
