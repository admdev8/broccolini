"""DataBaseOperation functions.

DataBase operations.
"""
import logging
from typing import Tuple, Any
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

    # def send_twilio_notification(self, **kwargs: str) -> str:
    # def fauna_add_to_database(self, **kwargs: str) -> bool:
    #     """Add to the database.

    #     write data to random database created in other method
    #     returns
    #     output_value: success
    #     output_type: bool
    #     minimum we need is a collection then an index then a record
    #     this record will come from the file data generated elsewhere
    #     """
    #     client = self.get_fauna_connection()
    #     # database: str = kwargs["database"]
    #     database_name_temp: str = 'satnightdb'
    #     collection_name = kwargs["collection_name"]
    #     data_to_add = kwargs["data_to_add"]
    #     # need to get database ref id correct it is currently using "collection=Ref(id=databases)"
    #     # instead of the correct name
    #     try:
    #         # query = client.query(q.get(q.database(database)))
    #         # query = client.query(q.create_database({"name": database_name_temp}))
    #         query = client.query(q.get(q.database(database_name_temp)))
    #         try:
    #             # collection_name_generated = client.query(q.collection(collection_name))
    #             # collection_name_generated = client.query(q.create_collection({"name": collection_name}))
    #             # collection_name_generated = client.query(q.create_collection({"name": "collectionmanual1"}))
    #             query = client.query(q.get(q.database(database_name_temp)))
    #             fauna_client.query2(q.create_collection({"name": collection_name}))
    #             # ient.query(q.create_collection({"name": "posts"}))
    #             # logging.debug(collection_name_generated)
    #             # logging.debug(database)
    #             logging.debug(data_to_add)
    #             return True

    #         except BadRequest as _error:  # pragma: no cover
    #             raise ValueError("Fauna error collection create.") from _error
    #     except (Exception) as _error:  # pragma: no cover
    #         raise ValueError("Fauna error.") from _error


# serverClient.query(
#   q.create_index(
#     {
#       "name": "posts_by_title",
#       "source": q.collection("posts"),
#       "terms": [{"field": ["data", "title"]}]
#     }
#   ))
