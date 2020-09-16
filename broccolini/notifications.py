"""Notification functions.

Notification functions including twilio.
"""
import logging

from twilio.base.exceptions import TwilioException, TwilioRestException
from twilio.rest import Client

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class TwilioFunctions:
    """Twilio Functions.

    Authentication and secrets from Hashicorp Vault.
    Vault credentials used to retrieve twilio settings.
    input: account_sid - from vault data
    input_type: str
    input: auth_token - from vault data
    input_type: str
    """

    def __init__(self, account_sid: str, auth_token: str) -> None:
        """Init class - vars are called in the function as needed."""
        self.account_sid = account_sid
        self.auth_token = auth_token

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    # def get_twilio_connection(self, **kwargs: str) -> Client:
    def get_twilio_connection(self) -> Client:
        """Get twilio connection.

        input: vault credentials from environment variables
        input_type: str
        output: twilio connection
        output_type: Client
        """
        try:
            client = Client(self.account_sid, self.auth_token)
            return client
        except TwilioRestException as error:  # pragma: no cover
            return f"exception as {error}"

    def send_twilio_notification(self, **kwargs: str) -> str:
        """Send notification.

        input: twilio client
        input_type: Client
        input: message_body
        input_type: str
        input: twilio_phone_number
        input_type: str
        input: twilio_notification_number
        input_type: str
        side effect: text to twilio_notification_number
        output: message_sid
        output_type: str
        """
        message_body = f'written directories: {kwargs["written_directories"]}'
        twilio_phone_number = kwargs["twilio_phone_number"]
        twilio_notification_number = kwargs["twilio_notification_number"]
        client = self.get_twilio_connection()
        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_phone_number,
                to=twilio_notification_number,
            )
            return f"successful message_sid:{message.sid}:"
        except (TwilioException, TwilioRestException) as _error:  # pragma: no cover
            raise ValueError(
                "Permission Denied, please check your permissions and the path to the secret!"
            ) from _error
