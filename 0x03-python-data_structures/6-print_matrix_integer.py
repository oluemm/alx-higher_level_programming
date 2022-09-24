#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for items in matrix:
        for mat in items:
            print("{:d}".format(mat), end=" ")
        print("")
