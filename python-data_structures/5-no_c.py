def no_c(my_string):
    string =""
    for letra in my_string:
        if letra != "c" and letra != "C":
            string += letra
    return string

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
