from collections.abc import Generator
from typing import Optional

from ..project_typing._typing import WriteFileState
from ..schema.capcha_code_response import CodeList

__all__ = ["CaptchaCodeDownloader"]


class CaptchaCodeDownloader:
    API_MAX_COUNT = 135

    def __init__(
        self,
        config_path: str,
        target_quantity: int,
        file_extend: Optional[str] = ".png",
    ) -> None:
        from ..config.download import DownloadConfig

        self.config = DownloadConfig.set_model_config(
            {
                "env_file": config_path,
                "env_file_encoding": "UTF-8",
            }
        )()  # type: ignore
        self.target_quantity = target_quantity
        self.file_extend = file_extend

    @property
    def files_in_folder(self) -> Generator[str, None, None]:
        from os import listdir
        from os.path import isfile, join

        return (
            file
            for file in listdir(self.config.root_path)
            if isfile(path=join(self.config.root_path, file))
        )

    @property
    def file_count(self) -> int:
        if self.file_extend:
            return len(
                [
                    file
                    for file in self.files_in_folder
                    if file.endswith(self.file_extend)
                ]
            )

        else:
            return len(list(self.files_in_folder))

    @property
    def remaining_quantity(self) -> int:
        return self.target_quantity - self.file_count

    @property
    def now_max_worker(self) -> int:
        from ..utils import calculate_max_quantity

        return calculate_max_quantity(
            max_count=self.remaining_quantity,
            base_num=self.API_MAX_COUNT,
        )

    def _parse_response_to_codelist(self) -> Optional[set[CodeList]]:
        if self.remaining_quantity < 0:
            print("<0")
            return None

        from ..service.captcha_code_pic_service import fetch_captcha_code_url

        captchas: set[CodeList] = set()

        while self.target_quantity >= len(captchas):
            captchas.update(
                fetch_captcha_code_url(self.config.captcha_code_pic_url).codelist
            )
        return captchas

    async def pipeline(self) -> Optional[list[WriteFileState]]:
        from asyncio import gather

        from ..service.captcha_code_pic_service import async_write_captcha_code_pic

        if all_codelist := self._parse_response_to_codelist():
            states = await gather(
                *[
                    async_write_captcha_code_pic(
                        root_path=self.config.root_path,
                        text=codelist.code,
                        filename=f"{codelist.ans}_{codelist.__hash__()}.png",
                    )
                    for codelist in all_codelist
                ]
            )

            return states

        return None
