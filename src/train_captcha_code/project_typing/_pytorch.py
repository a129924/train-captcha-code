from torch import Tensor
from typing_extensions import NamedTuple

__all__ = ["CaptchaItem"]


class CaptchaItem(NamedTuple):
    """
    image: Tensor
    label_index: Tensor
    label_name: str
    """

    image: Tensor
    label_index: Tensor
    label_name: str
