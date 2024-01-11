#!/usr/bin/env python3
"""Type Checking"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of list of floats and integers

    Args:
        mxd_lst (List[Union[int, float]]): list of floats and integers

    Returns:
        float: sum of list of floats and integers
    """
    return sum(mxd_lst)
