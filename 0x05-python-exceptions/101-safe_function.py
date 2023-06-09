#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        args: The arguments for fct.

    Returns:
        None-if an error occurs.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
