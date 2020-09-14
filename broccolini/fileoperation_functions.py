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
    def build_dictionary(**kwargs: Path) -> Dict[str, object]:
    # def build_dictionary(**kwargs: List[Dict[str, object]]) -> Dict[str, object]:
        """Builds dictionary of values.

        input: input_list list of directories to process
        input_type: str
        output: output_dict
        output_type: dict
        dictionary includes:
        subject - from pathlib
        modification date - from pathlib
        list of files run pathlib command to get list of files

        """
        input_path: Path = kwargs["input_path"]

        # list_of_files_and_folders: List[str] = []
        # logging.debug(type(input_path))
        # print(input_path.name)
        # subject = input_path.name
        # list_of_files_and_folders = list(input_path.rglob("*.*"))
        # logging.debug(list_of_files_and_folders)
        # logging.debug('\n')
        output_dict = dict(
            subject=input_path.name,
            folders_and_files=list(input_path.rglob("*.*")),
        )
        # output_dict = dict(subject=input_path.name, list_of_files_and_folders=)
        # list(input_path.rglob("*.*"),)
        logging.debug(output_dict)

    @staticmethod
    def get_file_information_build(
        **kwargs: str,
    ) -> List[Dict[str, object]]:
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
        logging.debug(folder_list)

        output_listing: List[Dict[str, object]] = []
        for each in folder_list:
            # logging.debug(type(each))
            write_to_json: Dict[str, object] = FileOperationFunctions.build_dictionary(
                input_path=each
            )
            # sending a path not a list
            logging.debug(each)
            logging.debug('\n')

            # not sending a list acting on each file in the for loop
            # collecting data in write to json
            # then writing write_to_json to json file on distk
            output_listing.append(write_to_json)
        logging.debug(output_listing)
        return output_listing

