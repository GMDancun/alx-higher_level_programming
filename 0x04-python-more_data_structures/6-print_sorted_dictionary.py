#!/usr/bin/python3i
# a function that prints a dictionary by ordered keys.


def print_sorted_dictionary(a_dictionary):
    ordered_dict = sorted(a_dictionary)
    for each_dict in ordered_dict:
        print("{}: {}".format(each_dict, a_dictionary[each_dict]))
