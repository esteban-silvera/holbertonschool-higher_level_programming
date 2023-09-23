#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        print(f"{x} arguments.")
    elif x == 1:
        print(f"{x} arguments:")
    else: 
        print(f"{x} arguments")
    for cantidad in range(x):
        print("{}: {}".format(cantidad, sys.argv[cantidad +1]))
