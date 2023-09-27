#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    nombres = dir(hidden_4)
    for x in nombres:
        if x[:2] != "__":
            print(f"{x}")
            