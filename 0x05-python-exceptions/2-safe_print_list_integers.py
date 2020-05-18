#!/usr/bin/python3
def safe_print_list_integers(my_list=[], r=0):
    printt = 0
    for iterator in range(0, r):
        try:
            print("{:d}".format(my_list[iterator]), end="")
            printt += 1
        except (ValueError, TypeError):
            continue
    print()
    return printt
