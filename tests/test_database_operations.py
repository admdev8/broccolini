#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Database operations functions.

Testing common Database operations. Starting with www.faunadb.com.
"""

import logging
from faunadb.client import FaunaClient

from broccolini.database_operations import DataBaseOperationFunctions

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestDatabaseOperationsFunctions:
    """Test Database Operation Functions.

    Build test directory with data.
    """

    @staticmethod
    def test_fauna_first(return_data_dict):
        """Test Fauna DB Connection"""
        result = DataBaseOperationFunctions.fauna_first(
            fauna_secret_path=return_data_dict["fauna_secret_path"],
        )
        logging.debug(result)
        expected = "fauna_secret_path1conftest"
        expected_type, expected_len = str, 2
        assert expected in str(result)
        assert isinstance(result, expected_type)
        assert len(result) >= expected_len
