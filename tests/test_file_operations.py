#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing file operations functions.

Testing common file operations including use of pathlib..
"""
# import os
# from os import mkdir
# from os import path
import logging
from pathlib import Path
from faker import Faker

# from faker.providers import file
from broccolini.fileoperation_functions import FileOperationFunctions

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


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
        # print(create_list_of_filenames_and_directories)
        for each in create_list_of_filenames_and_directories[0]:
            object_path = Path(each)
            # print(object_path)
            try:
                Path(object_path.parent).mkdir(parents=True, exist_ok=True)
                object_path.open("w")
                # object_path.write_text('asdfksdfldsjf asdfdsfdfs')
                object_path.write_text(fake.text())
                # run file operation functions with the temp directory created
            except (FileNotFoundError, FileExistsError) as _error:
                raise ValueError("Problem with file or directory!") from _error
        # test_directory = create_list_of_filenames_and_directories[1]
        # logging.debug(test_directory)

    @staticmethod
    def test_open_directory_begin_processing(return_data_dict):
        """Get the test directory from conftest to run tests."""
        result = FileOperationFunctions().open_directory_begin_processing(
            input_directory=return_data_dict["faker_files"],
            output_file_name=return_data_dict["output_file_name"],
        )
        expected = r"fake_data_from_conftest/training/"
        expected_type, expected_len = list, 3
        assert expected in str(result)
        assert isinstance(result, expected_type)
        assert len(result) >= expected_len
        # logging.debug(result)

    @staticmethod
    def test_build_dictionary(return_a_list):
        """Get the test directory from conftest to run tests."""
        result = FileOperationFunctions().build_dictionary(
            input_list=return_a_list,
        )
        logging.debug(result)
        # logging.debug(return_a_list)
        expected_type = dict
        assert isinstance(result, expected_type)
