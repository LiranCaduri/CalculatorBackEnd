def addition(number2, number1):
    return number1 + number2


def substruct(number2, number1):
    return number1 - number2


def multiply(number2, number1):
    return number1 * number2


def division(number2, number1):
    try:
        return number1 / number2
    except ZeroDivisionError as exception:
        return exception

def get_calculation_methods():
    operations = {
        "+": addition,
        "-": substruct,
        "*": multiply,
        "/": division,
    }
    
    return operations
