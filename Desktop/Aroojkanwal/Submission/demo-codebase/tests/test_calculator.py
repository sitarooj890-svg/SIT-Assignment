import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, subtract, multiply, divide, power, modulo, square, cube

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # We WANT a ValueError, not a ZeroDivisionError
    try:
        divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_power():
    assert power(2, 3) == 8


def test_power_zero():
    assert power(5, 0) == 1


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_by_zero():
    try:
        modulo(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_square():
    assert square(4) == 16


def test_square_float():
    assert square(2.5) == 6.25


def test_cube():
    assert cube(3) == 27


def test_cube_float():
    assert cube(2.5) == 15.625
