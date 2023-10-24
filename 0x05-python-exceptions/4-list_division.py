#!/usr/bin/python3
# a function that divides element by element 2 lists.....


def list_division(my_list_1, my_list_2, list_length):
    mynew_list = []
    for listx in range(0, list_length):
        try:
            divofno = my_list_1[listx] / my_list_2[listx]
        except TypeError:
            print("wrong type")
            divofno = 0
        except ZeroDivisionError:
            print("division by 0")
            divofno = 0
        except IndexError:
            print("out of range")
            divofno = 0
        finally:
            mynew_list.append(divofno)
    return (mynew_list)
