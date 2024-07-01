from pydantic import model_validator
from typing_extensions import Self

from .base import BaseConfig


class TrainConfig(BaseConfig):
    train_ratio: float
    test_ratio: float
    batch_size: int

    @model_validator(mode="after")
    def check_ratios(self) -> Self:
        if (self.train_ratio + self.test_ratio) == 1.0:
            return self

        raise ValueError("train_ratio 加 test_ratio 必須等於 1")
