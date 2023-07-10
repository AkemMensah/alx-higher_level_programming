#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (any): the object to add an attribute to.
        att (str): the name of the attribute to add to obj.
        value (any): the value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
