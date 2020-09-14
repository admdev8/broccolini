"""FileOperation functions.

File operations, eg, open close read write.
"""

import logging
from pathlib import Path
from typing import List, Dict, Sequence
from broccolini.json_functions import JsonFunctions

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
    def build_dictionary(**kwargs: List[str]) -> Dict[str, Sequence[str]]:
        """Builds dictionary of values.

        input: pathlib data
        input_type: str
        output: dictionary of values
        output_type: dict
        """
        input_list: List[str] = kwargs["input_list"]
        # input_list = self.input_list
        # logging.debug(input_list)
        output_dict = dict(
            subject=input_list,
            filename_of_dir_listing="filename_recursive_dir",
            # subject="subject data", filename_of_dir_listing="filename_recursive_dir",
        )
        return output_dict

    @staticmethod
    # def open_directory_build_db_of_metadata(**kwargs: str) -> List[Path]:
    def open_directory_build_db_of_metadata(
        **kwargs: str,
    ) -> List[Dict[str, Sequence[str]]]:
        """Build data about file structure."""
        input_directory: str = kwargs["input_directory"]
        output_file_name: str = kwargs["output_file_name"]
        path = Path(input_directory)
        folder_list = [_ for _ in path.iterdir()]
        output_listing = []
        for each in folder_list:
            # print(f" each in folder list {build_dictionary(each)}")
            write_to_json = FileOperationFunctions.build_dictionary(input_list=each)
            output_listing.append(write_to_json)
        logging.debug(output_listing)
        # logging.debug(write_to_json)
        return output_listing
