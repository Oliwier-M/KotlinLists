import pytest
import line2d
import math


def test_line2d_init_error():
    with pytest.raises(TypeError):
        line2d.Line2d('1', '2', '3')

    with pytest.raises(ValueError):
        line2d.Line2d(0, 2, 3)
        line2d.Line2d(1, 0, 3)
        line2d.Line2d(0, 0, 3)


def test_line2d_init_typical():
    assert isinstance(line2d.Line2d(1, 2, 3), line2d.Line2d)
    assert isinstance(line2d.Line2d(1, 2, 0), line2d.Line2d)


def test_angle_boundary():
    assert line2d.Line2d(1, 1, 1).angle(line2d.Line2d(1, 1, 1)) == 0
    assert line2d.Line2d(1, 1, 1).angle(line2d.Line2d(1, 1, 0)) == None


def test_angle_typical():
    pass


def test_angle_error():
    with pytest.raises(ValueError):
        assert line2d.Line2d(1, 1, 1).angle(line2d.Line2d(-1, 1, 1)) == math.tan(math.pi / 2)

    with pytest.raises(TypeError):
        assert line2d.Line2d(1, 1, 1).angle(-1, 1, 1) == math.tan(math.pi / 2)


def test_is_on_line_typical():
    assert line2d.Line2d(1, 1, 1).is_on_line(1, 1) is False
    assert line2d.Line2d(1, 1, 1).is_on_line(2, -1) is True


def test_is_on_line_boundary():
    pass


def test_is_on_line_error():
    with pytest.raises(TypeError):
        assert line2d.Line2d(1, 1, 1).is_on_line('a', 2)
