#!/usr/bin/python3
"""Base class instantiated"""
import json


class Base():
    """Base class for almost a circle tasks
    """
    __nb_objects = 0  # private class attrib: id tracker

    def __init__(self, id=None):  # instantiate an object
        if id is not None:  # check if id is given
            self.id = id  # assign id
        else:
            #  type(self) is used to initialize the private class attrib
            type(self).__nb_objects += 1  # auto assign id if not given
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        return json.dumps(f"{list_dictionaries}")
