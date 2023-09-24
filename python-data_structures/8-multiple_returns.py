def multiple_returns(sentence):
    if sentence == None:
        return None
    x = len(sentence)
    print("Length: {} - First character: {}".format(x, sentence[0]))

sentence = "At school, I learnt C!"
multiple_returns(sentence)