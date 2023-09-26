#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listi = my_list
    for num in my_list:
        if num == search:
            listi[num] = replace
    return listi
