#!/usr/bin/python3
"""Base class instantiated"""


class Base():
    __nb_objects = 0  # private class attrib: id tracker

    def __init__(self, id=None):  # instantiate an object
        if id != None:  # check if id is given
            self.id = id  # assign id
        else:
            #  type(self) is used to initialize the private class attrib
            type(self).__nb_objects += 1  # auto assign id if not given
            self.id =  type(self).__nb_objects
