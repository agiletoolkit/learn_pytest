# FizzBuzz is a common coding challenge used in programming interviews.
# - For multiples of 3, print "Fizz" instead of the number.
# - For multiples of 5, print "Buzz" instead of the number.
# - For numbers that are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import fizz_buzz

def test_fizz_buzz_number_return():
    assert fizz_buzz.buzzy_boy(1) == '1'
    assert fizz_buzz.buzzy_boy(2) =='2'
    assert fizz_buzz.buzzy_boy(8) =='8'
    
def test_fizz_buzz_fizzy():
    assert fizz_buzz.buzzy_boy(3)=='Fizz'
    assert fizz_buzz.buzzy_boy(6)=='Fizz'
    assert fizz_buzz.buzzy_boy(5)=='Buzz'
    assert fizz_buzz.buzzy_boy(10)=='Buzz'
    
def test_fizz_and_buzz ():
    assert fizz_buzz.buzzy_boy(15)=='FizzBuzz'
    assert fizz_buzz.buzzy_boy(30)=='FizzBuzz'