"""Json functions.

Json functions.  Mostly wrappers.
"""

import json
import logging
from typing import Dict, Tuple

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class JsonFunctions:
    """Json Functions."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def write_list_to_json(**kwargs: str) -> Tuple[bool, str]:
        """Convert a python list to a Json file.

        input: list
        input_type: list
        output side effect: json output in a json file
        output: success or failure
        output_type: bool
        """
        input_list = kwargs["input_list"]
        output_file_name: str = kwargs["output_file_name"]
        with open(output_file_name, "w") as file_handle:
            json.dump(input_list, file_handle)
        return True, f"successfully wrote file:{output_file_name}"

    @staticmethod
    def open_json_file_as_dict(**kwargs: str) -> Dict[str, str]:
        """Open json file from disk and return a python dictionary.

        input: input_file_name
        input_type: str
        output: values_from_file
        output_type: dict
        """
        input_file_name = kwargs["input_file_name"]

        with open(input_file_name) as file_handle:
            contents: Dict[str, str] = json.load(file_handle)
        return contents
