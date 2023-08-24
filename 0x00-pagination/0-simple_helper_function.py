#!/usr/bin/env python3
"""module contains simple helper function"""
from typing import Tuple, Dict


def index_range(page: int, page_size: int, **kwargs: Dict[str, int]) -> Tuple:
    """
        The function should return a tuple of size two containing a start
        index and an end index.
    """

    if kwargs:
        page = kwargs.get('page')
        page_size = kwargs.get('page_size')

        return ((page - 1) * page_size, page * page_size)
