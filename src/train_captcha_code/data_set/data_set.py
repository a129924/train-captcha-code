from functools import cached_property

from torch import Tensor
from torchvision import transforms
from typing_extensions import override

from ..project_typing._typing import LabeledFile
from .base import DataSetBase

__all__ = ["CaptchaDataSet"]


class CaptchaDataSet(DataSetBase[tuple[Tensor, str]]):
    def __init__(
        self,
        config_path: str,
        transform: transforms.Compose = transforms.Compose([transforms.ToTensor()]),
    ):
        from ..config.captcha_data_set import CaptchaDatasetConfig

        self.config = CaptchaDatasetConfig.set_model_config(
            {
                "env_file": config_path,
                "env_file_encoding": "UTF-8",
            }
        )()  # type: ignore
        self.transform = transform

    @cached_property
    def target_img_files_and_labels(self) -> list[LabeledFile]:
        from os.path import join

        from ..utils import get_files_in_folder

        return [
            LabeledFile(
                target_file=join(self.config.captcha_code_pic_path, file),
                label=file.split("_", 1)[0],
            )
            for file in get_files_in_folder(
                path=self.config.captcha_code_pic_path,
                file_extension=self.config.target_file_extension,
            )
        ]

    @override
    def __len__(self) -> int:
        return len(self.target_img_files_and_labels)

    @override
    def __getitem__(self, index: int) -> tuple[Tensor, str]:
        from PIL.Image import open as pil_open

        labeled_file = self.target_img_files_and_labels[index]

        return (
            self.transform(pil_open(labeled_file.target_file).convert("RGB")),  # type: ignore
            labeled_file.label,
        )
