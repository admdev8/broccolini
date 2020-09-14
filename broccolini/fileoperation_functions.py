"""FileOperation functions.

File operations, eg, open close read write.
"""

import logging
from pathlib import Path
from typing import List, Dict
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
    def open_directory_build_db_of_metadata(**kwargs: str) -> List[Path]:
        """Build data about file structure."""
        input_directory: str = kwargs["input_directory"]
        output_file_name: str = kwargs["output_file_name"]
        path = Path(input_directory)
        folder_list = [_ for _ in path.iterdir()]
        # print(f'folder list type is {folder_list}')
        for each in folder_list:
            print(f" each in folder list {build_dictionary(each)}")

        # output_dict = dict(
        # subject="subject",
        # filename_we_wrote_to_that_has_recursive_dir_listing="filename_recursive_dir",
        # )
        # # {"subject": "subject", "filename_we_wrote_to_that_has_recursive_dir_listing": "filename_recursive_dir"}
        # # logging.debug(output_dict)
        # # logging.debug(output_file_name)
        # # write output_dict to json file here
        # try:
        #     message_from_func = JsonFunctions().write_list_to_json(
        #         input_list=output_dict,
        #         output_file_name=output_file_name,
        #     )

        #     # return True, output_file_name
        #     logging.debug(message_from_func)
        #     return True, message_from_func
        # except Exception as _error:
        #     raise ValueError("Problem writing file") from _error


def build_dictionary(input_list: List[str]) -> Dict[str, str]:
    """Builds dictionary of values.

    Returns:
        [output_dict]: [description]
    """
    output_dict = dict(
        subject="subject data",
        filename_we_wrote_to_that_has_recursive_dir_listing="filename_recursive_dir",
    )
    logging.debug(input_list)
    logging.debug(type(output_dict))
    return output_dict["subject"]

    # return output_dict
