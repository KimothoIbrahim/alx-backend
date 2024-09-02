#!/usr/bin/env python3
"""Simple helper function"""

def index_range(page: int, page_size: int) -> (int, int):
    """
    args: page: int
          page_size: int
    Returns: A tuple of Integers
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
