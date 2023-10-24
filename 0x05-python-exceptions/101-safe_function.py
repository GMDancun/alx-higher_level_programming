#!/usr/bin/python3
# a function that executes a function safely....


import sys
def safe_function(fct, *args):
    try:
        prls = fct(*args)
    except ZeroDivisionError:
        prls = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        prls = None
        sys.stderr.write("Exception: list index out of range\n")

    return prls
