#!/usr/bin/python3
# a function that returns a new dictionary with all values multiplied by 2


def multiply_by_2(a_dictionary):
    return {elm: a_dictionary[elm] * 2 for elm in a_dictionary}
