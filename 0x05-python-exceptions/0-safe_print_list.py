#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end='')  # print each element at index i
            count += 1  # keeping count of items in my_list
        except IndexError:  # catch errors relating to list indexing
            break
    print("")  # to add a new line
    return (count)
