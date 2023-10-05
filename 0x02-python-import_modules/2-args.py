#!/usr/bin/python3
# write a program that prints the no. of and the last digit of its argumements
if __name__ == '__main__':
    import sys
    noof_arg = len(sys.argv) - 1
    if noof_arg == 0:
        print('{} arguments.'.format(noof_arg))
    else:
        print('{} arguments:'.format(noof_arg))
        for arg in range(1, noof_arg+1):
            print("{}: {}".format(arg, sys.argv[arg]))
