from slugify import MAX_LENGTH, slugify


def test_lowercases_and_joins_words_with_hyphens():
    assert slugify("Hello World") == "hello-world"


def test_drops_punctuation_and_keeps_word_boundaries():
    assert slugify("What's New, Doc?") == "what-s-new-doc"


def test_transliterates_accented_characters():
    assert slugify("Café Münster") == "cafe-munster"


def test_collapses_runs_of_separators_to_one_hyphen():
    assert slugify("a   ---   b") == "a-b"


def test_truncates_to_max_length():
    assert len(slugify("chapter " * 20)) <= MAX_LENGTH


def test_truncated_slug_does_not_end_in_a_hyphen():
    assert not slugify("chapter " * 20).endswith("-")


def test_title_without_alphanumerics_yields_an_empty_slug():
    assert slugify("!!! ???") == ""
