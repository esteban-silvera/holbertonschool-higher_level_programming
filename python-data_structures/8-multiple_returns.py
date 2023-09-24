#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        return None
    x = len(sentence)
    first = sentence[0]
    return (x, first)
