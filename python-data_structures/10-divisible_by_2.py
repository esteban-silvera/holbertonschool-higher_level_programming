#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    listarda = []
    for nums in my_list:
        if nums % 2 == 0:
            listarda.append(True)
        else:
            listarda.append(False)
        return listarda
