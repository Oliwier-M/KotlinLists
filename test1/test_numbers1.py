import pytest
from numbers1 import yet_the_largest


def test_yet_the_largest_typical():
    assert yet_the_largest([2, 91, -15, 90, -10, 101, 56]) == [2, 91, 101]


def test_yet_the_largest_boundary():
    assert yet_the_largest([]) == []
    assert yet_the_largest([1.0]) == [1.0]
    assert yet_the_largest([1, 1, 1]) == [1]


def test_yet_the_largest_error():
    with pytest.raises(TypeError):
        yet_the_largest(1, 2, 3)
