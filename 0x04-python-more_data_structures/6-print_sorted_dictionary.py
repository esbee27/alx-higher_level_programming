#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictn = sorted(a_dictionary)
    for i in sorted_dictn:
        print("{:s}: {}".format(i, a_dictionary[i]))
