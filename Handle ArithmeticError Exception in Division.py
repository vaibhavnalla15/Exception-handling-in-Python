""" Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error. """
# exception ArithmeticError:
# The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError.

def division(a, b):
    try:
        result = a / b
        print("Result", result)
    except ArithmeticError:
        print("Error: Arithmetic error occurred!")

dividend = float(input("Enter a dividend:- "))
divisor = float(input("Enter a divisor:- "))

division(dividend, divisor)