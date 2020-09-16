"""DataBaseOperation functions.

DataBase operations.
"""
import logging
from faunadb.client import FaunaClient
from faunadb import query as q
# from faunadb.objects import Ref


logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class DataBaseOperationFunctions:
    """DataBase Operation Functions.

    Authentication and secrets from Hashicorp Vault.
    Vault credentials used to retrieve twilio settings.
    input: client_token - from vault data
    input_type: str
    """

    def __init__(self, client_token: str) -> None:
        """Init class - vars are called in the function as needed."""
        self.client_token = client_token

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    def get_fauna_connection(self) -> FaunaClient:
        """Get Fauna Connection.

        input: client_token from class
        input_type: str
        output: fauna database connection
        output_type: FaunaClient
        """
        try:
            client = FaunaClient(secret=self.client_token)
            return client
        except Exception as _errorinfo:  # pragma: no cover
            raise ValueError("error connecting") from _errorinfo

    def fauna_read_database(self) -> FaunaClient:
        """Read from fauna database."""
        client = self.get_fauna_connection()
        indexes = client.query(q.paginate(q.indexes()))
        return indexes
