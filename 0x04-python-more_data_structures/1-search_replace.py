#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    x = new_list.replace(search, replace)
    print(x)
