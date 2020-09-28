"""API Access functions.

API Access functions.
"""
import logging
from typing import Dict
import requests


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class ApiAccess:
    """Process such as psutil."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def return_statistics_from_api(**kwargs: str) -> Dict[str, str]:
        """Connect to an Application Programming Interface.
        input: api_url
        input_type: str
        input: api_url
        input_type: str

        output: output_data
        output_type: Dict[str, str]
        """
        api_url: str = kwargs["api_url"]
        api_key: str = kwargs["api_key"]
        headers = {"Authorization": f"Bearer {api_key}"}
        # print(headers)

        with requests.Session() as session:
            session.headers.update(headers)
            response = session.get(api_url)
            if response.status_code != 200:
                raise ValueError("Issue with url or authentication.")
                # print(f'failure:{api_url}:')
            return response

    #         # def fetch(session, csv):
    #         with requests.Session() as session:
    #             # r = requests.get('<MY_URI>', headers={'Authorization': 'TOK:<MY_TOKEN>'})
    #             # api_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/"

    #         access_token = #yourAccessTokenHere#

    # result = requests.post(url,
    #       headers={'Content-Type':'application/json',
    #                'Authorization': 'Bearer {}'.format(access_token)})

    #             with session.get(api_url) as response:
    #                 data = response.text
    #                 return data
    #     if response.status_code != 200:
    #         print(f'failure:{}"FAILURE::{0}".format(url))
    # logging.debug(data)
    #     # Return .csv data for future consumption
    #     # return data

    # return dict(
    #     api_url=api_url,
    #     api_key=api_key,
    # )

    @staticmethod
    def return_statistics_from_api_updated() -> str:
        """View Running Processes."""
        return "dummy_string"
        # input_data: str = kwargs["input_data"]
        # return input_data
