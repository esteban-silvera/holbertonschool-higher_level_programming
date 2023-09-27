#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    largo = len(argv) - 1
    total = 0
    for x in range(largo):
        total += int(argv[x + 1])
    print("{}".format(total))
