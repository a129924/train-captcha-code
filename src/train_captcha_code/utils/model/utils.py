from torch.utils.data import DataLoader, Dataset, Subset, random_split

from ...project_typing._typing import DatasetSplitSizes, T

__all__ = ["get_train_size_and_test_size", "split_data_set", "create_loader"]


def get_train_size_and_test_size(
    train_ratio: float,
    dataset_size: int,
) -> DatasetSplitSizes:
    train_size = int(dataset_size * train_ratio)

    return DatasetSplitSizes(train_size=train_size, test_size=dataset_size - train_size)


def split_data_set(
    data_set: Dataset[T], split_sizes: DatasetSplitSizes
) -> list[Subset[T]]:
    return random_split(
        dataset=data_set, lengths=[split_sizes.train_size, split_sizes.test_size]
    )


def create_loader(
    data_set: Dataset[T],
    batch_size: int,
    shuffle: bool,
) -> DataLoader[T]:
    return DataLoader(dataset=data_set, batch_size=batch_size, shuffle=shuffle)
