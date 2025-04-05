import pytest
from app import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3  
    assert add(-1, -1) == -2  
    assert add(0, 0) == 0  

def test_subtract():
    assert subtract(5, 3) == 2  
    assert subtract(0, 5) == -5  
    assert subtract(-5, -5) == 0 

def test_multiply():
    assert multiply(2, 3) == 6  
    assert multiply(-2, 3) == -6  
    assert multiply(0, 10) == 0  

def test_divide():
    assert divide(10, 2) == 5  
    assert divide(-10, 2) == -5  
    with pytest.raises(ValueError):
        divide(10, 0)