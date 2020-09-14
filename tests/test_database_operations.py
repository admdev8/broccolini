#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Database operations functions.

Testing common Database operations. Starting with www.faunadb.com.
"""

import logging

from broccolini.database_operations import DataBaseOperationFunctions

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestDatabaseOperationsFunctions:
    """Test Database Operation Functions.

    Build test directory with data.
    """

    @staticmethod
    def test_fauna_first():
        """Test Fauna DB Connection"""
        result = DataBaseOperationFunctions.fauna_first()
        logging.debug(result)
        # expected = r"fake_data_from_conftest/training/"
        # expected_type, expected_len = list, 3
        # assert expected in str(result)
        # assert isinstance(result, expected_type)
        # assert len(result) >= expected_len
