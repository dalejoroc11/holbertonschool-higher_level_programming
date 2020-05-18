#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printd = 0
    for iterator in range(x):
        try:
            print("{:d}".format(my_list[iterator]), end="")
            printd += 1
        except:
            continue
    print()
    return printd
