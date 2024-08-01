#!/usr/bin/env python3
"""
    type-annotated function floor which takes a float n as argument
    and returns the floor of the float.
"""
import math


def floor(n:float) -> int:
    """ floor method returns the floor of n """
    return int(math.floor(n))
