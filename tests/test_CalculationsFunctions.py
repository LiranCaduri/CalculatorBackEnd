from src.CalculationsFunctions import (
    get_calculation_methods, addition, substruct, multiply, division)


def test_get_calculation_methods():
    operations = {
        "+": addition,
        "-": substruct,
        "*": multiply,
        "/": division,
    }

    assert get_calculation_methods() == operations

def test_addition():
    assert addition(110, 10) == 120
    assert addition(0.001, 10.11) == 10.110999999999999


def test_substruct():
    assert substruct(10, 5) == 5
    assert substruct(10, 0.1) == 9.9


def test_multiply():
    assert multiply(10, 10) == 100
    assert multiply(10, 0.1) == 1


def test_division():
    assert type(division(10, 0)) == ZeroDivisionError
    assert division(112, 5) == 22.4
    assert division(120, 10) == 12

