from collections.abc import Generator

from ..schema.verification_code_response import VerificationCodeResponse
from ..utils.fetch import fetch_url


def fetch_verification_code_url(url: str) -> VerificationCodeResponse:
    return VerificationCodeResponse(**fetch_url(url))


def get_verification_code_pic_content(
    verification_code_response: VerificationCodeResponse,
) -> Generator[tuple[str, str], None, None]:
    return (
        (codelist.ans, fetch_url(f"data:image/png;base64,{codelist.code}"))
        for codelist in verification_code_response.codelist
    )


def write_verification_code_pic(
    contents: Generator[tuple[str, str], None, None],
) -> None:
    from os.path import join

    from ..utils.file import write_file

    root = "./verification_code_pic"

    for ans, content in contents:
        write_file(text=content, out_filapath=join(root, f"{ans}.png"))
