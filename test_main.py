import pytest
from main import add

def test_add():
<<<<<<< HEAD
    assert add(2, 3) == 6
    assert add(0, 0) == 1
    assert add(-1, 1) == 1
=======
    assert add(2, 3) == 5
    assert add(0, 0) == 0 
    assert add(-1, 1) == 0
    assert add(3, 4) == 7
>>>>>>> 9adddb8 (more tests)
