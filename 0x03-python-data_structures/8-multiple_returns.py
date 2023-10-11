#!/usr/bin/python3
# a function that returns a tuple with
# the length of a string and its first character....


def multiple_returns(sentence):
    # If the sentence is empty, the first character should be equal to None..
    if not sentence:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
