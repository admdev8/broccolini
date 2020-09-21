#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing json functions using classes.

Testing json operations.  Mostly wrappers.
"""
import logging
from broccolini.json_functions import JsonFunctions

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestJsonFunctions:
    """Test Json Functions."""

    @staticmethod
    def test_write_list_to_json(return_a_list, create_generic_json_test_file):
        """Test write list to json file with list."""
        result = JsonFunctions().write_list_to_json(
            input_list=return_a_list,
            output_file_name=create_generic_json_test_file,
        )
        expected = "generic_file_name_json"
        expected_type = tuple
        assert expected in result[1]
        assert isinstance(result, expected_type)

    @staticmethod
    def test_open_json_file_as_dict(
        create_dir_to_simulate_json_bulk_load_orig,
    ):
        """Test open json file."""
        input_file_name = create_dir_to_simulate_json_bulk_load_orig
        result = JsonFunctions().open_json_file_as_dict(input_file_name=input_file_name)
        expected_type = dict
        expected = "website_from_conftest"
        assert result["website"] == expected
        assert isinstance(result, expected_type)
