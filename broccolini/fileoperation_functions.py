"""FileOperation functions.

File operations, eg, open close read write.
"""

import logging
from pathlib import Path
from typing import List, Dict, Sequence

# from broccolini.json_functions import JsonFunctions

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class FileOperationFunctions:
    """File Operation Functions."""

    def __init__(self) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    @staticmethod
    def build_dictionary(**kwargs: List[Dict[str, object]]) -> Dict[str, object]:
        """Builds dictionary of values.

        input: pathlib data
        input_type: str
        output: dictionary of values
        output_type: dict
        """
        input_list: List[Dict[str, object]] = kwargs["input_list"]
        # input_list: List[str] = kwargs["input_list"]
        # input_list = self.input_list
        logging.debug(type(input_list))
        output_dict = dict(
            subject=input_list,
            filename_of_dir_listing="filename_recursive_dir",
            # subject="subject data", filename_of_dir_listing="filename_recursive_dir",
        )
        return output_dict

    @staticmethod
    def open_directory_begin_processing(**kwargs: str,) -> List[Dict[str, object]]:
        """Build data about file structure.

        input: input_directory
        input_type = input_directory
        output: output_listing
        output_type = List[str]
        """
        input_directory: str = kwargs["input_directory"]
        path = Path(input_directory)
        folder_list: List[Path] = []
        for each in path.iterdir():
            folder_list.append(each)
        # output_listing: List[Dict[str, object]] = []
        output_listing: List[Dict[str, object]] = []
        # output_listing: List[Dict[str, Sequence[str]]] = []
        for each in folder_list:
            # print(type(each))
            write_to_json: Dict[str, object] = FileOperationFunctions.build_dictionary(
                input_list=each
            )
            output_listing.append(write_to_json)
        logging.debug(type(output_listing))
        return output_listing
