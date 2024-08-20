import pytest
import shingle


def test_shingle():
    # idk how to test that
    with pytest.raises(TypeError):
        shingle.read('1', '5')

    with pytest.raises(ValueError):
        shingle.read(3, 0)
        shingle.read(2, -1)


def test_shingle_typical():
    assert isinstance(shingle.read(3, 3), type(shingle.read()))
    assert isinstance(shingle.read(5, 2), type(shingle.read()))

# how do I test with input text?
def test_shingle_boundary():
    assert shingle.read(2, 2)  == #??? I can't know what it should equal, because I don't have the input

# def test_
