#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4 as hidden
    name = dir(hidden)
    for ite in range(len(name)):
        if name[ite][:2] != '__':
            print("{:s".format(name[ite]))
