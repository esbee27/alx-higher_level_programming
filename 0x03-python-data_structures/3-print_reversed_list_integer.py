#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_len = len(my_list)
    my_list.reverse()
    for j in range(my_list_len):
        print("{:d}".format(my_list[j]))
