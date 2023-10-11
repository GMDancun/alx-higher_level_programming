#!/usr/bin/python3
# a function that removes all characters c and C from a string....
def no_c(my_string):
    char2_string = ""
    for char2 in my_string:
        if char2 != 'c' and char2 != 'C':
            char2_string = char2_string + char2
    return char2_string
