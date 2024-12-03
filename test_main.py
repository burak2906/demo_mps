import pytest
from main import add

def test_add():
    assert add(2, 3) == 6
    assert add(0, 0) == 0
    assert add(-1, 1) == 1
