#!/usr/bin/python3
def safe_print_integer(value):
    counter = 0
    for iterator in range(x):
        try:
            print('{:d}'.format(my_list[iterator]), end='')
            counter += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            raise
    print()
    return counter
