from torch.utils.data import Dataset

from ..project_typing._typing import T

__all__ = ["DataSetBase"]


class DataSetBase(Dataset[T]):
    @classmethod
    def __len__(cls) -> int:
        """
        必須定義資料集長度
        """

        raise NotImplementedError(f"'{cls.__name__}.__len__()' must be defind")
