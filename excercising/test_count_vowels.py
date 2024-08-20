import pytest
from count_vowels import count_vowels


def test_count_vowels_error():
    with pytest.raises(TypeError):
        count_vowels(5)
        count_vowels(True)
        count_vowels(3.0)
        count_vowels(['1', 'twe', 'rk'])


def test_count_vowels_typical():
    assert count_vowels("And you test this") == 5


def test_count_vowels_boundary():
    assert count_vowels("") == 0
    assert count_vowels("aeuioiooioi") == 11
    assert count_vowels("rrrrrr") == 0
    assert count_vowels("a") == 1
