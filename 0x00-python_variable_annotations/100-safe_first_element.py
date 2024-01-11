#!/usr/bin/env python3
"""Type Checking"""
from typing import Union, Any, List


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """Returns a value or none"""
    if lst:
        return lst[0]
    else:
        return None
