#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)-1
    print(count, " arguments: ")
    for items in enumerate(sys.argv):
        if items[0] == 0:
            pass
        else:
            print(f"{items[0]}: {items[1]}")
