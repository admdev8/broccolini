#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing Database operations functions.

Testing common Database operations. Starting with www.faunadb.com.
"""

import logging
import pytest
from faunadb.client import FaunaClient
from broccolini.authentication_functions import VaultFunctions
from broccolini.database_operations import DataBaseOperationFunctions

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TestDatabaseOperationsFunctions:
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
        except KeyError as _error:
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
        client_token = TestDatabaseOperationsFunctions.get_test_values(
            return_data_dict["fauna_secret_path"]
        )
        # need to filter client token to only give the data we need here
        result = DataBaseOperationFunctions(
            client_token=client_token
        ).get_fauna_connection()
        expected = "faunadb.client.FaunaClient"
        expected_type = FaunaClient
        assert expected in str(result[0])
        assert isinstance(result[0], expected_type)
        logging.debug(result)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_fauna"])
    def test_fauna_read_database(return_data_dict):
        """Test login to fauna."""
        client_token = TestDatabaseOperationsFunctions.get_test_values(
            return_data_dict["fauna_secret_path"]
        )
        # logging.debug(client_token)
        result = DataBaseOperationFunctions(
            client_token=client_token
        ).fauna_read_database()
        logging.debug(result)
