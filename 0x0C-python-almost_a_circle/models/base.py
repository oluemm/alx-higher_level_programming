#!/usr/bin/python3
"""Base class instantiated"""
import json
import csv


class Base():
    """Base class for almost a circle tasks

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

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
            If json_string is None or empty- an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            else:
                instance = cls(1)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        #  create a filename using the class.__name__ special method
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:  # open the json file
                #  export instance dicts to list
                list_dicts = Base.from_json_string(jsonfile.read())
                # return instances for each dictionary
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"  # auto-generated filename
        # open file for writing
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:  # check for empty list
                csvfile.write("[]")
                return
            # checking class instances and assigning appropriate fieldnames
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in list_objs:  # picking instances out of the list
                # writing dict representation of instances to csv file
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return the deserialization of a CSV file.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            # open file for reading
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    #  use dictreader to read fields values
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                #  create a list of instance dictionaries of each row
                list_dicts = [
                    dict(
                        [k, int(v)] for k, v in row.items()
                        )for row in list_dicts
                    ]
                # create instance of the saved dicts
                return [cls.create(**instance) for instance in list_dicts]
        except IOError:
            return []
