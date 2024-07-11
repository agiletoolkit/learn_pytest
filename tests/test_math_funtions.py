import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import math_functions

def test_add():
    assert math_functions.add(1,2)==3

def test_mult():
    assert math_functions.multiply(2,3)==6
    
def test_mult2():    
    assert math_functions.multiply(3,3)==9