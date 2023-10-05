#!/usr/bin/python3
# a program that prints the result of the addition of all args
if __name__ == "__main__":
    import sys

    totalarg = 0
    for arg in range(len(sys.argv) - 1):
        totalarg += int(sys.argv[arg + 1])
    print("{}".format(totalarg))
