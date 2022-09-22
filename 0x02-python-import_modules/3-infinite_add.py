#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    for items in sys.argv[1:]:
        sum += int(items)
    print(sum)
