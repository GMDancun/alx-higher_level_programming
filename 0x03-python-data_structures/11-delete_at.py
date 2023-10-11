#!/usr/bin/python3
# a function that deletes the item at a specific position in a list...
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    newmy_list = []
    for eachitem in range(len(my_list)):
        if eachitem != idx:
            newmy_list.append(my_list[eachitem])
    return newmy_list
