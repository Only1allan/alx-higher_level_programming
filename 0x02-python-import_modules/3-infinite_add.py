#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv
    summ = 0
    for i in range(argv[1:]):
        summ += int(i)
    print("{:d}".format(summ))
