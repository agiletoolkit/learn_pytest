import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import my_fun

def test_add():
    assert my_fun.add(1,2)==3

def test_mult():
    assert my_fun.mult(2,3)==6
    
def test_mult2():    
    assert my_fun.mult(3,3)==5