#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    h = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            h += 1
        except:
            pass
        print()
        return h
