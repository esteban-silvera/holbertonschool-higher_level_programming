#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listarda = []
    for nums in my_list:
        if nums % 2 == 0:
            listarda[nums] = True
        else:
            listarda[nums] = False
        return listarda
