#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing file operations functions.

Testing common file operations including use of pathlib..
"""
import logging
from pathlib import Path
import pytest

from faker import Faker

from broccolini.fileoperation_functions import FileOperationFunctions

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestFileOperationsFunctions:
    """Test File Operation Functions.

    Build test directory with data.
    """

    @staticmethod
    def test_build_files_with_faker(
        create_list_of_filenames_and_directories,
    ):
        """Open directory to generate test data.

        This should probably be moved to conftest.  This creates a folder
        structure and generates files.
        Saved a copy of this in data_from_faker_precomputed
        data_from_faker_precomputed = r'./tests/fake_data_from_conftest/training'
        regenerate this data manually if necessary
        """
        fake = Faker("en_US")
        for each in create_list_of_filenames_and_directories[0]:
            object_path = Path(each)
            try:
                Path(object_path.parent).mkdir(parents=True, exist_ok=True)
                object_path.open("w")
                object_path.write_text(fake.text())
            except (FileNotFoundError, FileExistsError) as _error:
                raise ValueError("Problem with file or directory!") from _error

    @staticmethod
    def test_get_file_information_build(return_data_dict):
        """Get the test directory from conftest to run tests."""
        result = FileOperationFunctions().get_file_information_build(
            input_directory=return_data_dict["faker_files"],
            output_file_name=return_data_dict["output_file_name"],
        )
        expected = r"fake_data_from_conftest/training/"
        expected_type, expected_len = list, 3
        assert expected in str(result)
        assert isinstance(result, expected_type)
        assert len(result) >= expected_len

    @staticmethod
    @pytest.fixture()
    def test_build_dictionary_of_files(create_list_of_filenames_and_directories):
        """Get the test directory from conftest to run tests.

        Gets folder path from conftest and feeds to the function as a pathlib object
        """
        result = FileOperationFunctions().build_dictionary(
            input_path=Path(create_list_of_filenames_and_directories[1]),
        )
        expected = "test_dir_created"
        expected_type, expected_len = dict, 9
        assert expected in str(result)
        assert isinstance(result, expected_type)
        assert len(result["folders_and_files"]) >= expected_len
        return result

    @staticmethod
    def test_filter_file_data(test_build_dictionary_of_files):
        """Filter data from the data provided by the other function."""
        # logging.debug(test_build_dictionary_of_files)
        result = FileOperationFunctions().filter_file_data(
            input_path=test_build_dictionary_of_files,
        )
        expected_type = list
        assert isinstance(result, expected_type)
        # logging.debug(result["subject"])
        for each in result:
            print(f"{each}\n")
        # logging.debug(result)
