from typing import Literal

from typing_extensions import TypedDict


class WriteFileState(TypedDict):
    filepath: str
    state: Literal["success", "failed"]
