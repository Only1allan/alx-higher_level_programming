#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    new_list = set(my_list)
    for i in new_list:
        addition += i
    return addition
