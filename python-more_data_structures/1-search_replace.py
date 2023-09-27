#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listi = []
    for num in my_list:
        if num == search:
            listi.append(replace)
        else:
            listi.append(num)
    return listi
