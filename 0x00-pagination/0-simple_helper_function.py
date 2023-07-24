#!/usr/bin/env python3
"""function named index_range
    Returns:
        a tuple of size two containing a start index and an end
        index corresponding to the range of indexes to return in a list
    """

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    start index and an end index corresponding to the range of
    """
    return ((page-1) * page_size, page_size * page)
