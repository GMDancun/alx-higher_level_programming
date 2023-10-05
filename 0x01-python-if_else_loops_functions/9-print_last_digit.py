#!/usr/bin/python3
# a func that prints the last digit of a num
def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
