from typing import Literal

from typing_extensions import NamedTuple, TypedDict


class WriteFileState(TypedDict):
    filepath: str
    state: Literal["success", "failed"]


class LabeledFile(NamedTuple):
    target_file: str
    label: str
