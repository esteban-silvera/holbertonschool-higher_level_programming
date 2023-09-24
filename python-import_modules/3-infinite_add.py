#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for x in range(len(argv) - 1):
        total += int(argv[x + 1])
    print("{}".format(total))
