from typing import Optional


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
