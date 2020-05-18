#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resultdiv = a / b
    except:
        resultdiv = None
    finally:
        print("Inside result: {}".format(resultdiv))
    return resultdiv
