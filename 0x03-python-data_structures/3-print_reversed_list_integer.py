#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return(None)
        rev = my_list[:]
        rev.rev()
        for iterator in rev:
            print('{:d}'.format(iterator))
