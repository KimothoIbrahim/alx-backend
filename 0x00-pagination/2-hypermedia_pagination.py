#!/usr/bin/env python3
"""Simple helper function"""

import csv
import math
from typing import List, Dict


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
        """Make and return page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        tup = index_range(page, page_size)
        if self.__dataset is None:
            self.dataset()
        if tup[0] > len(self.__dataset):
            return []
        if self.__dataset:
            return self.__dataset[tup[0]:tup[1]]

    def get_hyper(
                  self, page: int = 1,
                  page_size: int = 10
    ) -> Dict[str, int | List]:
        """HyperMedia
        """
        hyper_media = {}

        data = self.get_page(page, page_size)
        hyper_media['page_size'] = len(data)
        hyper_media['page'] = page
        hyper_media['data'] = data

        tup = index_range(page, page_size)
        print(len(self.__dataset))
        print(tup)
        if tup[1] > (len(self.__dataset) - 1) or tup[1] == 0:
            hyper_media['next_page'] = None
        else:
            hyper_media['next_page'] = page + 1
        if page - 1 > 0:
            hyper_media['prev_page'] = page - 1
        else:
            hyper_media['prev_page'] = None
        if len(self.__dataset) % page_size:
            (hyper_media['total_pages'] = int(len(self.__dataset) / page_size) + 1)
        else:
            hyper_media['total_pages'] = int(len(self.__dataset) / page_size)
        return hyper_media
