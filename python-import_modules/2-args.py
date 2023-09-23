#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("1 arguments:")
    else: 
        print(f"{x} arguments")
    for cantidad in range(x):
        print("{}: {}".format(cantidad, sys.argv[cantidad]))
