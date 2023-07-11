#!/usr/bin/python3
"""Defines a Python class-to-JSON funct."""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure."""
    return obj.__dict__
