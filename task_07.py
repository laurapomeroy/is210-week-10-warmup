#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function that returns a funky value"""

DATA = {
    234: 41414,
    321: 8392,
    90: 378,
    909: 12,
    222: 1234,
    99: 2039,
    39: 948,
    999: 120,
    322: 9849,
    9829: 12,
    3029: 1,
    3: 2931
}


def iter_dict_funky_sum(mydict):
    """Takes one dictionary argument, extracts the key pairs, assigns
and appends

    Args:
        mydict(dictionary): a dictionary, both keys and values are integers.

    Returns:
        Returns a funky total

    Examples:
    >>> task_07.iter_dict_funky_sum(task_07.DATA)
    >>>43164

    """
    total = 0
    for key, value in mydict.iteritems():
        total += value - key
    return total
