#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [str(i).replace(str(search), str(replace)) for i in my_list]
    return new_list