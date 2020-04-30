#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumar = 0
    if len(sys.argv) is 1:
        print("{}".format(sumar))
    elif len(sys.argv) > 1:
        for x in range(1, len(sys.argv)):
            sumar = sumar + int(sys.argv[x])
        print("{}".format(sumar))
