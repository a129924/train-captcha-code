from collections.abc import AsyncGenerator

from ..project_typing._typing import WriteFileState
from ..schema.capcha_code_response import CaptchaCodeResponse

__all__ = ["CaptchaCodeDownloader"]


class CaptchaCodeDownloader:
    API_MAX_COUNT = 135

    def __init__(self, config_path: str, limit_file_count: int) -> None:
        from ..config.download import DownloadConfig

        self.config = DownloadConfig.set_model_config(
            {
                "env_file": config_path,
                "env_file_encoding": "UTF-8",
            }
        )()  # type: ignore
        self.limit_file_count = limit_file_count

    @property
    def max_worker(self) -> int:
        from os import listdir

        from ..utils import calculate_max_quantity

        return calculate_max_quantity(
            max_count=self.limit_file_count
            - len(listdir(self.config.captcha_code_pic_path)),
            base_num=self.API_MAX_COUNT,
        )

    def _parse_response(self) -> list[CaptchaCodeResponse]:
        from ..service.captcha_code_pic_service import fetch_captcha_code_url

        return [
            fetch_captcha_code_url(self.config.captcha_code_pic_url)
            for _ in range(self.max_worker)
        ]

    async def pipeline(self) -> AsyncGenerator[list[WriteFileState], None]:
        from asyncio import gather

        from ..service.captcha_code_pic_service import async_write_captcha_code_pic

        while self.max_worker > 0:
            captcha_code_responses = self._parse_response()

            states = await gather(
                *[
                    async_write_captcha_code_pic(
                        root_path=self.config.root_path,
                        text=codelist.code,
                        filename=f"{codelist.ans}.png",
                    )
                    for captcha_code_response in captcha_code_responses
                    for codelist in captcha_code_response.codelist
                ]
            )

            yield states
