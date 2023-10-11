#!/usr/bin/python3
# a function that adds 2 tuples.
def add_tuple(tuple_a=(), tuple_b=()):
    tpla = tuple_a + (0, 0)
    tplb = tuple_b + (0, 0)
    return (tpla[0] + tplb[0], tpla[1] + tplb[1])
