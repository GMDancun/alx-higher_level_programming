#!/usr/bin/python3
# a function that finds the biggest integer of a list....
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for eachint in range(len(my_list)):
            if my_list[eachint] > max:
                max = my_list[eachint]
        return max
