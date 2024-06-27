from collections.abc import Generator
from os.path import join

from ..project_typing._typing import WriteFileState
from ..schema.capcha_code_response import CaptchaCodeResponse
from ..utils.sync.fetch import fetch_url_to_json


def fetch_captcha_code_url(url: str) -> CaptchaCodeResponse:
    return CaptchaCodeResponse(**fetch_url_to_json(url))


def write_verification_code_pics(
    root_path: str,
    cverification_code_response: CaptchaCodeResponse,
) -> Generator[WriteFileState, None, None]:
    from ..utils.sync._file import write_file_from_byte_string

    for codelist in cverification_code_response.codelist:
        yield write_file_from_byte_string(
            text=codelist.code,
            out_filapath=join(root_path, f"{codelist.ans}.png"),
        )


async def async_write_captcha_code_pic(
    root_path: str,
    text: str,
    filename: str,
) -> WriteFileState:
    from ..utils._async._file import write_file_from_byte_string

    return await write_file_from_byte_string(
        text=text, out_filapath=join(root_path, filename)
    )
