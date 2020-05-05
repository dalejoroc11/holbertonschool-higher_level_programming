#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if index < 0 or index >= len(my_list):
        return(my_list)
    else:
        n_list = my_list[:]
        n_list[idx] = element
        return(n_list)
