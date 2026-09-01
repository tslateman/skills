import pytest

from slug import slugify


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("Hello World", "hello-world"),
        ("  padded  ", "padded"),
        ("under_scores_too", "under-scores-too"),
        ("Café Münster", "cafe-munster"),
        ("multiple   spaces", "multiple-spaces"),
        ("punctuation!!! here?", "punctuation-here"),
        ("--leading and trailing--", "leading-and-trailing"),
    ],
)
def test_slugify_shapes(raw, expected):
    assert slugify(raw) == expected


def test_empty_input_gives_empty_slug():
    assert slugify("") == ""


def test_only_punctuation_gives_empty_slug():
    assert slugify("!!!???") == ""


def test_truncates_on_a_word_boundary():
    assert slugify("alpha beta gamma delta", max_length=12) == "alpha-beta"


def test_truncation_never_exceeds_max_length():
    assert len(slugify("a" * 200, max_length=20)) <= 20


def test_single_long_word_is_hard_cut_rather_than_emptied():
    assert slugify("supercalifragilistic", max_length=10) == "supercalif"
