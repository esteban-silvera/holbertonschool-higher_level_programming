#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        return None
    x = len(sentence)
    print("Length: {} - First character: {}".format(x, sentence[0]))
