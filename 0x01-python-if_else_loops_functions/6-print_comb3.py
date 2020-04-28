#!/usr/bin/python3
for iterator in range(0,10):
    for iterator2 in range(iterator + 1, 10):
        if(iterator != 8):
            print("{}{}".format(iterator,iterator2), end=", ")
        else:
            print("{}{}".format(iterator, iterator2))
