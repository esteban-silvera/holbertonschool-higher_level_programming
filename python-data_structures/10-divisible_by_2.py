#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listarda = []
    x = 0
    for nums in my_list:
        if nums % 2 == 0:
            listarda[x] = True
            x + 1
        else:
            listarda[x] = False
            x + 1
        return listarda
