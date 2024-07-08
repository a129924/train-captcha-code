from functools import lru_cache
from typing import Optional

__all__ = [
    "char_to_index",
    "calculate_max_quantity",
    "get_files_in_folder",
    "index_to_char",
]


def calculate_max_quantity(max_count: int, base_num: int) -> int:
    from math import ceil

    return ceil(max_count / base_num)


def get_files_in_folder(
    path: str,
    file_extension: Optional[str] = None,
) -> list[str]:
    from os import listdir

    if file_extension:
        return [file for file in listdir(path=path) if file.endswith(file_extension)]
    else:
        return listdir(path=path)


@lru_cache
def char_to_index() -> dict[str, int]:
    from string import ascii_letters, digits

    return {char: idx for idx, char in enumerate(f"{digits}{ascii_letters}")}


@lru_cache
def index_to_char() -> dict[int, str]:
    return {idx: char for char, idx in char_to_index().items()}
