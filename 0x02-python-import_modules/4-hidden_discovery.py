#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    for ite in range(len(names)):
        if names[ite][:2] != '__':
            print("{:s".format(names[ite]))
