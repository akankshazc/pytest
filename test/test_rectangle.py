import pytest

import source.shapes as shapes


def test_area(my_rectangle):
    assert my_rectangle.area() == 3 * 4


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (3 + 4)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle