#!/usr/bin/python3
# a function def roman_to_int(roman_string):
# that converts a Roman numeral to an integer.


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    
    the_roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    fin_result = 0
    r_value = 0
    
    for char in roman_string[::-1]:
        value = the_roman_dict[char]
        if value >= r_value:
            fin_result += value
        else:
            fin_result -= value
        r_value = value
    
    return fin_result
