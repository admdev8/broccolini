"""DataBaseOperation functions.

DataBase operations.
"""
import logging
from typing import List, Dict, Tuple, Any
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.errors import BadRequest
from faunadb.objects import Ref

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class DataBaseOperations:
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

    def fauna_create_database(self, **kwargs: str) -> Tuple[bool, Any, str]:
        """Create database.

        create random database with shortuuid to ensure randomness
        """
        client = self.get_fauna_connection()
        database: str = kwargs["database"]
        try:
            query = client.query(q.create_database({"name": database}))
            return True, query, database
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Unable to create database.") from _error

    def fauna_read_database(self) -> Dict[List[str], Any]:
        """Read from fauna database."""
        try:
            client = self.get_fauna_connection()
            indexes = client.query(q.paginate(q.indexes()))
            return indexes
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error - read database.") from _error

    def fauna_create_collection(self, **kwargs: str) -> bool:
        """Create collection."""
        client = self.get_fauna_connection()
        collection_name: str = kwargs["collection_name"]
        try:
            client.query(q.create_collection({"name": collection_name}))
            return True, collection_name
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_add_records(self, **kwargs: str) -> bool:
        """Add records.

        input: data to add
        input: test collection name
        returns:
            output: success or failure
            output type: bool
        """
        client = self.get_fauna_connection()
        records_to_add: str = kwargs["records_to_add"]
        collection_name: str = kwargs["collection_name"]
        try:
            return client.query(
                q.create(q.collection(collection_name), {"data": {"name": records_to_add, "element": ["air", "fire"]}})
            )
        except (Exception) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_delete_database(self, **kwargs: str) -> Tuple[bool, Any, str]:
        """Fauna delete database."""
        client = self.get_fauna_connection()
        database: str = kwargs["database"]
        try:
            return client.query(q.delete(q.database(database)))
        except (BadRequest) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error

    def fauna_paginate_database(self) -> Tuple[bool, Any, str]:
        """Fauna paginate database."""
        client = self.get_fauna_connection()
        # database: str = kwargs["database"]
        try:
            return client.query(q.paginate(Ref("databases")))
        except (BadRequest) as _error:  # pragma: no cover
            raise ValueError("Fauna error.") from _error
