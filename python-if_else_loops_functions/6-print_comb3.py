#!/usr/bin/python3
for x in range(10):
    for n in range(x + 1, 10):
        print("{}".format(str(x) + str(n)), end="")
        if int(str(x) + str(n)) < 89:
            print(", ", end="")
print("")
