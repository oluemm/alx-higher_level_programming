#!/usr/bin/python3
"""Module that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""
    if list_of_integers == []:  # return None for empty lists
        return None
    size = len(list_of_integers)  # get length of list given
    if size == 1:  # if it contains a single element
        return list_of_integers[0]  # return that element
    elif size == 2:
        return max(list_of_integers)  # return the maximum of both

    mid = size // 2  # define a mid point of the list
    peak = list_of_integers[mid]  # assume peak is array mid element
    bfor = mid - 1  # element before the mid-point
    after = mid + 1  # element after the mid-point
    # check if peak is > element bfor and after it
    if peak > list_of_integers[bfor] and peak > list_of_integers[after]:
        return peak
    # if peak is < element bfor, split list from begining to peak
    # and recursively search for new peak
    elif peak < list_of_integers[bfor]:
        return find_peak(list_of_integers[:mid])
    else:
        # peak is > element after, split list from element after peak to
        # the end and recursively search for new peak
        return find_peak(list_of_integers[after:])
