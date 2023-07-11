6-load_from_json_file.py
#!/usr/bin/python3
"""Defines a JSON file-reading funct."""
import json


def load_from_json_file(filename):
    """Creates a Python obj from a JSON file."""
    with open(filename) as f:
        return json.load(f)
