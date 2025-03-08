import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.my_module import add, subtract

def test_add():
    assert add(2, 3) == 5
def test_subtract():
    assert subtract(5, 3) == 2