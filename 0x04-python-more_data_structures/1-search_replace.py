#!/usr/bin/python3
def search_replace(my_list, search, replace):
    updated_list = []
    for eachelement in my_list:
        if eachelement == search:
            updated_list.append(replace)
        else:
            updated_list.append(eachelement)
    return updated_list
