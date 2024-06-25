from collections.abc import Generator

from ..project_typing._typing import WriteFileState
from ..schema.verification_code_response import VerificationCodeResponse
from ..utils.fetch import fetch_url_to_json


def fetch_verification_code_url(url: str) -> VerificationCodeResponse:
    return VerificationCodeResponse(**fetch_url_to_json(url))


def write_verification_code_pic(
    cverification_code_response: VerificationCodeResponse,
) -> Generator[WriteFileState, None, None]:
    from os.path import join

    from ..utils.file import write_file_from_byte_string

    root = "./verification_code_pic"

    for codelist in cverification_code_response.codelist:
        yield from write_file_from_byte_string(
            text=codelist.code,
            out_filapath=join(root, f"{codelist.ans}.png"),
        )
