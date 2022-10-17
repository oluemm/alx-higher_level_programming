#!/usr/bin/python3
"""Prints `My name is <first name> <last name>` to stdout."""

def say_my_name(first_name, last_name=""):
    """Prints *My name is <first name> <last name>* to stdout.

    Usage: say_my_name(first_name, last_name)

    Args:
        first_name (_type_): user's first name
        last_name (str, optional): user's last_name. Defaults to "".

    Raises:
        TypeError: if either `first_name` or `last_name` is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
