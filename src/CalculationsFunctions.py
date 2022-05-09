def addition(number1, number2):
    return number1 + number2


def substruct(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def division(number1, number2):
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
