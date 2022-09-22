#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv)-1
    if count == 0:
        print(count, 'arguments: ')
    elif count == 1:
        print(count, 'argument: ')
    else:
        print(count, 'arguments: ')

    for i in range(count):
        print(f'{i+1}: {sys.argv[i+1]}')
