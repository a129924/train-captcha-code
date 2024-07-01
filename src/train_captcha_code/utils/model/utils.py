from ...project_typing._typing import DatasetSplitSizes


def get_train_size_and_test_size(
    train_ratio: float,
    dataset_size: int,
) -> DatasetSplitSizes:
    train_size = int(dataset_size * train_ratio)

    return DatasetSplitSizes(train_size=train_size, test_size=dataset_size - train_size)
