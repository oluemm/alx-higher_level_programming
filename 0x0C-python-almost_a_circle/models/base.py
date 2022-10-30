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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        return json.dumps(f"{list_dictionaries}")

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [values.to_dictionary() for values in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
