#!/usr/bin/python3
for iterator in range(0,9):
    for iterator2 in range(iterator + 1, 10):
        if(iterator == 8):
            print("{:d}{:d}".format(iterator,iterator2))
            break
            print("{:d}{:d}".format(iterator, iterator2), end=", ")
