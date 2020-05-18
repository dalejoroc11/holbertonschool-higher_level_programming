#!/usr/bin/python3
def safe_print_integer(_list=[], rango=0):
    printt = 0
    for iterator in range(rango):
        try:
            print("{:d}".format(_list[iterator]), end="")
            printt += 1
        except:
            continue
    print()
    return printt
