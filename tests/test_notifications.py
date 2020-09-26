#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing notification files using classes.

Testing notifications including twilio.
"""
import logging

import pytest
from twilio.rest import Client

from broccolini.authentication_functions import VaultFunctions
from broccolini.notifications import TwilioFunctions

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class TestTwilioFunctions:
    """Test Twilio Functions."""

    @classmethod
    def get_test_values(cls, secret_path):
        """Build values needed for the test."""
        try:
            twilio_path_auth_token_key = VaultFunctions().query_vault_data(
                vault_url="VAULT_URL",
                vault_token="VAULT_TOKEN",
                secret_path=secret_path,
            )
            auth_token = twilio_path_auth_token_key["data"]["data"]["_key"]
            return auth_token
        except KeyError as _error:
            raise ValueError("Missing environment variables") from _error

    @staticmethod
    @pytest.mark.dependency(name="test_login_to_twilio")
    def test_get_twilio_connection(return_data_dict):
        """Test login to twilio.

        input: auth_token
        input_type: str
        twilio_path_auth_token="greg_production/twilio_data/TWILIO_AUTH_TOKEN",
        output: twilio client
        """
        account_sid = TestTwilioFunctions.get_test_values(return_data_dict["twilio_account_sid"])
        auth_token = TestTwilioFunctions.get_test_values(return_data_dict["twilio_auth_token"])
        result = TwilioFunctions(account_sid, auth_token).get_twilio_connection()
        expected_type = Client
        assert isinstance(result, expected_type)

    @staticmethod
    @pytest.mark.dependency(depends=["test_login_to_twilio"])
    def test_send_twilio_notification(return_data_dict):
        """Test send twilio notification."""
        auth_token = TestTwilioFunctions.get_test_values(return_data_dict["twilio_auth_token"])
        twilio_phone_number = TestTwilioFunctions.get_test_values(return_data_dict["twilio_phone_number"])
        account_sid = TestTwilioFunctions.get_test_values(return_data_dict["twilio_account_sid"])
        twilio_notification_number = TestTwilioFunctions.get_test_values(return_data_dict["twilio_notification_number"])
        this = TwilioFunctions(account_sid, auth_token)
        result = this.send_twilio_notification(
            written_directories=return_data_dict["written_directories"],
            twilio_phone_number=twilio_phone_number,
            twilio_notification_number=twilio_notification_number,
        )
        expected_type = str
        assert isinstance(result, expected_type)
