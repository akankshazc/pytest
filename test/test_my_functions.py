# Function based tests

import pytest
from source.my_functions import add, divide


def test_add():
    assert add(4, 6) == 10
    assert add(8, 12) == 20
    assert add(9, 27) == 36
    assert add(10, 15) == 25
    assert add(12, 15) == 27
    with pytest.raises(TypeError):
        add(12, 'a')


def test_divide():
    assert divide(4, 6) == 0.6666666666666666
    assert divide(8, 12) == 0.6666666666666666
    assert divide(9, 27) == 0.3333333333333333
    assert divide(10, 15) == 0.6666666666666666
    assert divide(12, 15) == 0.8
    with pytest.raises(ZeroDivisionError):
        divide(12, 0)
    with pytest.raises(TypeError):
        divide(12, 'a')


def test_add_strings():
    result = add('hello ', 'world')
    assert result == 'hello world'
