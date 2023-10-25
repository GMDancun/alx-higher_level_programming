#!/usr/bin/python3i
# a function that returns the weighted average...
# of all integers tuple (<score>, <weight>)...


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    return sum([mul(w[0], w[1]) for w in my_list]) / sum(w[1] for w in my_list)


def mul(w, z):
    return w * z
