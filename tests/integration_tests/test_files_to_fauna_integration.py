#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testing integration from files in directory to fauna database.

Used for tracking duplicate files.
Also used as a basis for testing file async functionality
"""

import logging
import pytest

from broccolini.authentication_functions import VaultFunctions
from broccolini.fileoperation_functions import FileOperationFunctions

from broccolini.database_operations import DataBaseOperations

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestIntegrationFileToFauna:
    """Test the integration from files to fauna database."""

    @classmethod
    def get_test_values(cls, secret_path):
        """Build values needed for the test."""
        try:
            fauna_secret_key = VaultFunctions().query_vault_data(
                vault_url="VAULT_URL",
                vault_token="VAULT_TOKEN",
                secret_path=secret_path,
            )
            return fauna_secret_key["data"]["data"]["_key"]
        except KeyError as _error:  # pragma: no cover
            raise ValueError("Missing environment variables") from _error

    @pytest.mark.skip(reason="integration testing")
    @pytest.fixture()
    def test_get_files_from_folder(self, return_data_dict):
        """Get list of files from the directory.

        input: folder_name

        output: list_of_files
        output_type: List[Dict['folders_and_files'][pathlib.WindowsPath]]
        """
        result = FileOperationFunctions().get_file_information_build(
            input_directory=return_data_dict["faker_files"],
            output_file_name=return_data_dict["output_file_name"],
        )
        return result

    @pytest.mark.skip(reason="integration testing")
    def test_write_files_to_fauna_db(self, return_data_dict, return_random_uuid, test_get_files_from_folder):
        """Put list of files into fauna database.

        input: list
        output or side effect: fauna database
        """
        collection_name = f"collection_{return_random_uuid}"
        client_token = TestIntegrationFileToFauna.get_test_values(return_data_dict["fauna_secret_path_server"])
        records_to_add = []
        result = test_get_files_from_folder
        for each in result:
            records_to_add.append(str(each["folders_and_files"]))

        DataBaseOperations(client_token=client_token).fauna_create_collection(
            collection_name=collection_name,
        )
        result = DataBaseOperations(client_token=client_token).fauna_add_records(
            collection_name=collection_name,
            records_to_add=records_to_add,
        )
        return result
