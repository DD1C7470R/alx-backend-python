#!/usr/bin/env python3
"""Type Checking"""
from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of int tuple"""
    return [(i, len(i)) for i in lst]
