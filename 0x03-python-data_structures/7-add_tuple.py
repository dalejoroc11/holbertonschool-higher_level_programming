#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = list(tuple_a)
    l_b = list(tuple_b)
    len1 = len(l_a)
    len2 = len(l_b)
    while len1 < 2:
        l_a.append(0)
        len1 += 1
    while len2 < 2:
        l_b.append(0)
        len2 += 1
    x = l_a[0] + l_b[0]
    y = l_a[1] + l_b[1]
    return(x, y)
