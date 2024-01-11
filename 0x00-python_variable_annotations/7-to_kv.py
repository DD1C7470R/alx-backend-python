#!/usr/bin/env python3
"""Type Checking"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of (k, v**2)"""
    return (k, v**2)
