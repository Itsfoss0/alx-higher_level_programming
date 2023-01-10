#!/usr/bin/python3

"""Student class to represent a student"""


class Student:
    """Defining student class """
    def __init__(self, first_name, last_name, age):
        """Student constructor
        Args:
            first_name(str)
            last_name(str)
            age(str)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrive information about an instance to json
        Args:
            attrs(list) -> List of attribute to be retrieved
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
