#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    index_uno = sentence[0] if length > 0 else None
    return (length, index_uno)
