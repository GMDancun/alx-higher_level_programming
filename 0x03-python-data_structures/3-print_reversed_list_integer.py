#!/usr/bin/python3
# a function that prints all integers of a list, in reverse order....
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for eachint in range(len(my_list)):
            print("{:d}".format(my_list[eachint]))
