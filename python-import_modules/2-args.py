#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x == 0:
        print(f"{x} arguments.")
    elif x == 1:
        print(f"{x} arguments:")
    else: 
        print(f"{x} arguments:")
    for cantidad in range(x):
        print("{}: {}".format(cantidad + 1, argv[cantidad +1]))
