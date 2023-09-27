#!/usr/bin/python3
def no_c(my_string):
    string =""
    for letra in my_string:
        if letra != "c" and letra != "C":
            string += letra
    return string
