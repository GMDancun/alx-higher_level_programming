#!/usr/bin/python3
# a function that finds all multiples of 2 in a list....
def divisible_by_2(my_list=[]):
    num_list = []
    for eachnum in range(len(my_list)):
        if my_list[eachnum] % 2 == 0:
            num_list.append(True)
        else:
            num_list.append(False)
    return num_list
