#!/usr/bin/python3
def safe_print_integers(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
        except(ValueError, TypeError):
            continue
    print()
    return i
