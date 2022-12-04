#!/usr/bin/python3
def multiple_returns(sentence):
    "Return the length of a tuple and the first element"
    if not sentence:
        return (0, None)
    return (len(tuple(sentence)), tuple(sentence)[0])
