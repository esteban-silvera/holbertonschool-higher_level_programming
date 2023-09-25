#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    x = len(sentence)
    first = sentence[0]
    return (x, first)
