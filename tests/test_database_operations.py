#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Database operations functions.

Testing common Database operations. Starting with www.faunadb.com.
"""

import logging
import pytest
from faunadb.client import FaunaClient
from broccolini.authentication_functions import VaultFunctions
from broccolini.database_operations import DataBaseOperations

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestDatabaseOperations:
    """Test Database Operation Functions.

    Build test directory with data.
    client_token = api_key_dict["data"]["data"]["_key"]
    client = Client(self.account_sid, self.auth_token)
    """

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

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_fauna")
    def test_get_fauna_connection(return_data_dict):
        """Test login to fauna.

        input: client_token
        input_type: str
        output_type: FaunaClient
        output example: <faunadb.client.FaunaClient object at 0x000002439xxxxx>
        """
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_admin"])
        result = DataBaseOperations(client_token=client_token).get_fauna_connection()
        expected = "faunadb.client.FaunaClient"
        expected_type = FaunaClient
        assert expected in str(result)
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_create_database(return_data_dict, return_random_uuid):
        """Test Fauna DB create."""
        database = f"database_{return_random_uuid}"
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_admin"])
        result = DataBaseOperations(client_token=client_token).fauna_create_database(
            database=database,
        )
        expected_type = tuple
        expected = "_conftest_"
        assert isinstance(result, expected_type)
        assert expected in result[2]

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_read_database(return_data_dict):
        """Test Fauna DB read."""
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_server"])
        result = DataBaseOperations(client_token=client_token).fauna_read_database()
        expected_type = dict
        expected = "id=all_storehouses"
        assert isinstance(result, expected_type)
        assert expected in str(result["data"])

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_create_collection(return_data_dict, return_random_uuid):
        """Test Fauna DB create collection."""
        collection_name = f"collection_{return_random_uuid}"
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_server"])
        result = DataBaseOperations(client_token=client_token).fauna_create_collection(
            collection_name=collection_name,
        )
        expected_0 = True
        expected_1 = "_conftest_"
        assert result[0] == expected_0
        assert expected_1 in result[1]

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_add_records(return_data_dict, return_random_uuid):
        """Test Fauna DB add records."""
        collection_name = f"collection_{return_random_uuid}"
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_server"])
        result = DataBaseOperations(client_token=client_token).fauna_add_records(
            collection_name=collection_name,
            records_to_add=return_data_dict["fauna_test_data"],
        )
        expected_type = dict
        expected = "id=collection_conftest_"
        assert isinstance(result, expected_type)
        assert expected in str(result["ref"])

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_delete_database(return_data_dict, return_random_uuid):
        """Test Fauna DB delete database."""
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_admin"])
        database = f"database_{return_random_uuid}"
        result = DataBaseOperations(client_token=client_token).fauna_delete_database(
            database=database,
        )
        expected_type = dict
        expected = "id=database_conf"
        assert isinstance(result, expected_type)
        assert expected in str(result)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_delete_database_exception(return_data_dict):
        """Test Fauna DB delete database exception."""
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_admin"])
        with pytest.raises(ValueError):
            DataBaseOperations(client_token=client_token).fauna_delete_database(
                database=return_data_dict["fauna_test_bad_database"],
            )

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_paginate_database(return_data_dict):
        """Test Fauna paginate database."""
        client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_admin"])
        result = DataBaseOperations(client_token=client_token).fauna_paginate_database()
        expected_type = dict
        expected = r"collection=Ref(id=databases"
        assert isinstance(result, expected_type)
        assert expected in str(result["data"])

    # @staticmethod
    # @pytest.mark.dependency(depends=["test_login_to_fauna"])
    # def test_fauna_delete_collection(return_data_dict, return_random_uuid):
    #     """Test Fauna DB delete collection.

    #     Problem to watch out for is making sure you are working on the correct collection
    #     and correct database.
    #     """
    #     collection_name = f"collection_{return_random_uuid}"
    #     client_token = TestDatabaseOperations.get_test_values(return_data_dict["fauna_secret_path_server"])
    #     result = DataBaseOperations(client_token=client_token).fauna_delete_collection(
    #         collection_name=collection_name,
    #         # client.query(q.delete(q.collection("dilapidated_huts")))
    #     )

    #     logging.debug(result)
    #     assert result == collection_name
