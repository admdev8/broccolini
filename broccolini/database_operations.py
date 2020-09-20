"""DataBaseOperation functions.

DataBase operations.
"""
import logging
from typing import List, Dict, Tuple, Any
import shortuuid
from faunadb import query as q
from faunadb.client import FaunaClient

# from faunadb.objects import Ref
# from faunadb.errors import BadRequest


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


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

    # def get_fauna_connection(self) -> FaunaClient:
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


    def fauna_create_database(self) -> Tuple[bool, Any, str]:
        """Create database.

        create random database with shortuuid to ensure randomness
        returns

        """
        database = f"test_db_{shortuuid.uuid()}"
        client = self.get_fauna_connection()
        try:
            query = client.query(q.create_database({"name": database}))
            return True, query, database
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Unable to create database.") from _error

    def fauna_read_database(self, **kwargs: str) -> Dict[List[str], Any]:
        """Read from fauna database."""
        client = self.get_fauna_connection()
        database: str = kwargs["database"]
        # collection_name: str = kwargs["collection_name"]
        try:
            indexes = client.query(q.paginate(q.indexes()))
            return indexes
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error - read database.") from _error

    def fauna_paginate_collection(self, **kwargs: str) -> Tuple[str, str]:
        """Paginate collection."""
        client = self.get_fauna_connection()
        database: str = kwargs["database"]
        collection_name: str = kwargs["collection_name"]
        return database, collection_name
        # try:
        #     indexes = client.query(q.paginate(q.indexes()))
        #     return indexes
        # except (Exception) as _error:  # pragma: no cover
        #     raise ValueError("Fauna error - read database.") from _error
