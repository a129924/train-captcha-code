from torch import Tensor
from typing_extensions import NamedTuple

__all__ = ["CaptchaItem"]


class CaptchaItem(NamedTuple):
    """
    image: Tensor
    label_index: Tensor
    filepath: str
    """

    image: Tensor
    label_index: Tensor
    filepath: str
