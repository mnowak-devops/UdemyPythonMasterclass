#Running your first basic test

import pytest

def my_func(x, y, z):
    return x + y + z

def test_result1():
    assert my_func(1, 2, 3) <= 5

def my_exception():
    div = 10 / 0
    return div

def test_result3():
    with pytest.raises(ZeroDivisionError):
        my_exception()