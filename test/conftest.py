import pytest

import source.shapes as shapes

# for function we can use fixtures


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=4, width=3)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length=5, width=6)
