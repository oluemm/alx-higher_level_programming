#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        no_value_error = True
    except ValueError as err:
        no_value_error = False
        print("Exception: ",err)
    return no_value_error
