#!/usr/bin/python3
# a function that prints x elements of a list.


def safe_print_list(my_list=[], x=0):
    listx = 0

    try:
        for l in my_list:
            if listx < x:
                print('{}'.format(my_list[listx]), end='')
                listx += 1

        print()
    except TypeError:
        pass
    finally:
        return listx
