#!/usr/bin/python3
# a function that divides 2 integers and prints the result.......


def safe_print_division(a, b):
    try:
        divofno = a / b
    except (TypeError, ZeroDivisionError):
        divofno = None
    finally:
        print("Inside result: {}".format(divofno))
    return (divofno)
