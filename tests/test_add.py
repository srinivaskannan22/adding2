import pytest
from src.mat import add,sub

def test_adding():
    assert add(5+3) == 8
    assert add(4,6)==10

def test_sub():
    assert sub(4,3)==1
    assert sub(5,7) ==-2
