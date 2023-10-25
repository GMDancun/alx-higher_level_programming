#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda w: list(map(lambda z: z**2, w)), matrix[:]))
