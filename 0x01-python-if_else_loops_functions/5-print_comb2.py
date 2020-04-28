#!/usr/bin/python3
for iterator in range(0, 100):
    if iterator < 99:
        print("{:02d}, ".format(iterator), end="")
    else:
        print("{:02d}".format(iterator))
