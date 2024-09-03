#!/usr/bin/env python3
"""Simple helper function"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> (int, int):
    """
    args: page: int
          page_size: int
    Returns: A tuple of Integers
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0, "Page must be graeter tahn Zero"
        assert page_size > 0, "Page_size must be graeter tahn Zero"
        tup = index_range(page, page_size)
        dataset = self.dataset()
        if tup[0] > len(dataset):
            return []
        if self.__dataset:
            return dataset[tup[0]:tup[1]]
