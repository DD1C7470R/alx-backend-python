#!/usr/bin/env python3
"""Type Checking"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns a value or none"""
    if lst:
        return lst[0]
    else:
        return None
