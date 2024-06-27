from collections.abc import Generator
from os.path import join

from ..project_typing._typing import WriteFileState
from ..schema.verification_code_response import VerificationCodeResponse
from ..utils.sync.fetch import fetch_url_to_json


def fetch_verification_code_url(url: str) -> VerificationCodeResponse:
    return VerificationCodeResponse(**fetch_url_to_json(url))


def write_verification_code_pics(
    cverification_code_response: VerificationCodeResponse,
) -> Generator[WriteFileState, None, None]:
    from ..utils.sync.file import write_file_from_byte_string

    root = "./verification_code_pic"

    for codelist in cverification_code_response.codelist:
        yield write_file_from_byte_string(
            text=codelist.code,
            out_filapath=join(root, f"{codelist.ans}.png"),
        )


async def async_write_verification_code_pic(
    text: str,
    filename: str,
) -> WriteFileState:
    from ..utils._async.file import write_file_from_byte_string

    root = "./verification_code_pic"

    return await write_file_from_byte_string(
        text=text, out_filapath=join(root, filename)
    )
