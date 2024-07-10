from torch import optim
from torch.nn import CrossEntropyLoss, Module
from torch.utils.data import DataLoader
from typing_extensions import Self

from .._logger import Logger
from ..data_set.base import DataSetBase
from ..project_typing._typing import T

__all__ = ["ModelBaseTrainer"]


class ModelBaseTrainer:
    logger = Logger

    def __init__(
        self,
        model: Module,
        dataset: DataSetBase,
        train_loader: DataLoader[T],
        test_loader: DataLoader[T],
        criterion: CrossEntropyLoss,
        *,
        learning_rate: float,
    ) -> None:
        self.model = model

        self.dataset = dataset
        self.train_loader = train_loader
        self.test_loader = test_loader

        self.criterion = criterion
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)

    def load_model_from_file(self, model_path: str) -> Self:
        from os.path import exists

        if exists(model_path):
            from torch import load

            self.model.load_state_dict(load(model_path))

        return self

    def train(self, model_save_path: str, *, num_epochs: int) -> Self:
        """
        train 模型訓練function interface

        Args:
            model_save_path (str): model 儲存的路徑
            num_epochs (int): 迭代次數

        Raises:
            NotImplementedError: 繼承後必須實作該interface

        Returns:
            Self: return self
        """
        raise NotImplementedError("train 必須被實作")

    def validate(self, num_epochs: int) -> Self:
        """
        train 模型驗證function interface

        Args:
            num_epochs (int): 迭代次數

        Raises:
            NotImplementedError: 繼承後必須實作該interface

        Returns:
            Self: return self
        """

        raise NotImplementedError("validate 必須被實作")
