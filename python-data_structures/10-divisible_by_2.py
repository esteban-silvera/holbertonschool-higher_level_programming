#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    listarda = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            listarda.append(True)
        else:
            listarda.append(False)
        return listarda
