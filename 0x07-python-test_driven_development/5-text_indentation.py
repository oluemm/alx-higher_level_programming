#!/usr/bin/python3
"""Define a function that modifes a string/text
"""


def text_indentation(text):
    """ Prints a text with 2 new lines after 
    each of these characters: `.`, `?` and `:`
    Args:
        text (string): The string to indent

    Returns: None

    Usage:
        text_indentation(text)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = text.replace('. ', '.\n\n').replace(': ', ':\n\n')\
        .replace('? ', '?\n\n')
    print(result)
