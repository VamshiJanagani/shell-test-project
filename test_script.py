import pytest

def add(a, b):
    return a + b

def test_addition():
    assert add(2, 3) == 5  #This is a test comment 2

def test_failing_case():
    assert add(2, 2) == 4  
