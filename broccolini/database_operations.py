"""DataBaseOperation functions.

DataBase operations.
"""
import logging
from typing import Tuple, Any
import shortuuid
from faunadb import query as q
from faunadb.client import FaunaClient

# from faunadb.errors import FaunaError, BadRequest

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

    def fauna_read_database(self) -> FaunaClient:
        """Read from fauna database."""
        client = self.get_fauna_connection()
        indexes = client.query(q.paginate(q.indexes()))
        return indexes

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

    def fauna_add_to_database(self) -> Tuple[bool, Any, str]:
            """Add to the database.

            write data to random database created in other method
            returns
            output_value: success
            output_type: bool
            """
            return True

# database = f"test_db_{shortuuid.uuid()}"
# fauna_add_to_database
    # def fauna_write_database(self) -> FaunaClient:
    #     """Write to fauna database.
    #     2020-09-16 00:01:01,436 - DEBUG -
    #     {'ref': Ref(id=froglegs01_new, collection=Ref(id=databases)),
    #     'ts': 1599661067450000, 'name': 'froglegs01_new', 'global_id': 'yxku95xzgydbg'
    #     """
    #     client = self.get_fauna_connection()
    #     database = "froglegs01_new"

    #     # return query
    #     try:
    #         # query = client.query(q.create_database({"name": database}))
    #         # delete it if it exists
    #         client.query(q.delete(q.database(database)))
    #         # if it deletes then recreate it
    #         # if it doesn't exist then don't try and delete it or return
    #         # create it now
    #         query = client.query(q.create_database({"name": database}))
    #         # try:
    #     #         query = client.query(q.create_database({"name": database}))
    #     #         return query
    #     #     except (BadRequest, FaunaError, Exception) as _error:  # pragma: no cover
    #     #         raise ValueError("Fauna error.") from _error
    #     except (BadRequest, Exception) as _error:  # pragma: no cover
    #         raise ValueError("Unable to delete database.") from _error
