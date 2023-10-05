#!/usr/bin/python3
# a py function def magic_calculation(a, b): that does the exact same as the py bytecode
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for nums in range(4, 6):
            c = add(c, nums)
