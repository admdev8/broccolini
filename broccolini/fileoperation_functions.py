"""FileOperation functions.

File operations, eg, open close read write.
"""

import logging
from pathlib import Path
from typing import List

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
        path = Path(input_directory)
        folder_list = [_ for _ in path.iterdir()]
        return folder_list
