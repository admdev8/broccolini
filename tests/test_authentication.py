#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing authentication functions."""
import logging

import hvac
import pytest

from broccolini.authentication_functions import VaultFunctions

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestVaultFunctions:
    """Test Vault Functions."""

    @staticmethod
    @pytest.mark.skip(reason="needs mock")
    def test_unseal_vault():
        """Test unseal vault."""
        result = VaultFunctions().unseal_vault(
            vault_url="VAULT_URL",
            vault_token="VAULT_TOKEN",
            vault_unseal_token="VAULT_UNSEAL_TOKEN",
        )
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert result == expected

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_vault")
    def test_login_to_vault():
        """Test login to vault.

        input : vault settings
        output: vault client connection
        """
        result = VaultFunctions.get_vault_credentials(vault_url="VAULT_URL", vault_token="VAULT_TOKEN")
        expected = "hvac.v1.Client object at 0"
        expected_type = hvac.v1.Client
        assert isinstance(result, expected_type)
        assert expected in str(result)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_vault"])
    def test_login_to_vault_exception_bad_vault_url():
        """Test vault login exception.

        input : deliberately bad vault settings
        output: none
        """
        message = "Missing environment variables"
        with pytest.raises(ValueError, match=message):
            VaultFunctions.get_vault_credentials(vault_url="VAULT_URL_BAD", vault_token="VAULT_TOKEN_BAD")

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_vault"])
    def test_query_vault_data(return_data_dict):
        """Test query to vault.

        input : successful client
        input: secret_path: dict path to secret
        output: output of secret : str
        result = client.read(path)  # gets all variables at this path
        """
        result = VaultFunctions().query_vault_data(
            vault_url="VAULT_URL",
            vault_token="VAULT_TOKEN",
            secret_path=return_data_dict["secret_path"],
        )
        result_key = result["data"]["data"]["secret_test_key"]
        expected_type = dict
        expected = "secret_value_from_conftest"
        assert isinstance(result, expected_type)
        assert expected in result_key

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_vault"])
    def test_add_to_vault(return_data_dict):
        """Test add vault data."""
        result = VaultFunctions().add_to_vault(
            vault_url="VAULT_URL",
            vault_token="VAULT_TOKEN",
            secret_path=return_data_dict["secret_path"],
            secret=return_data_dict["secret"],
        )
        expected_type = tuple
        expected_1 = "202"
        creation_time = result[1]["data"]["created_time"]
        assert expected_1 in creation_time
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_vault"])
    def test_initialized_vault():
        """Test that vault is initialized."""

        result = VaultFunctions().initialized_vault(
            vault_url="VAULT_URL",
            vault_token="VAULT_TOKEN",
        )
        expected = True
        expected_type = bool
        assert isinstance(result, expected_type)
        assert result == expected
