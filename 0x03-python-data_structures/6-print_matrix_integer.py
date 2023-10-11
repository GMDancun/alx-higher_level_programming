#!/usr/bin/python3
# a function that prints a matrix of integers....
def print_matrix_integer(matrix=[[]]):
    for eachrow in matrix:
        for eachcol in eachrow:
            print("{:d}".format(eachcol), end=" " if eachcol != eachrow[-1] else "")
        print()
