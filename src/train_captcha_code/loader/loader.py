from functools import cached_property
from typing import Generic

from torch.utils.data import DataLoader, Subset

from ..data_set.base import DataSetBase
from ..project_typing._typing import T
from ..utils.model import create_loader


class CaptchaLoader(Generic[T]):
    def __init__(self, config_path: str, dataset: DataSetBase[T]) -> None:
        from ..config.train_config import TrainConfig

        self.config = TrainConfig.set_model_config(
            model_config={"env_file": config_path, "env_file_encoding": "UTF-8"}
        )()  # type: ignore

        self.dataset = dataset

    @cached_property
    def train_loader(self) -> DataLoader[T]:
        return create_loader(
            data_set=self._split_dataset()[0],
            batch_size=128,
            shuffle=True,
        )

    @cached_property
    def test_loader(self) -> DataLoader[T]:
        return create_loader(
            data_set=self._split_dataset()[1],
            batch_size=128,
            shuffle=False,
        )

    def get_loaders(self) -> tuple[DataLoader[T], DataLoader[T]]:
        return (self.train_loader, self.test_loader)

    def _split_dataset(self) -> list[Subset[T]]:
        from ..utils.model import get_train_size_and_test_size, split_data_set

        return split_data_set(
            data_set=self.dataset,
            split_sizes=get_train_size_and_test_size(
                train_ratio=self.config.train_ratio,
                dataset_size=len(self.dataset),
            ),
        )
