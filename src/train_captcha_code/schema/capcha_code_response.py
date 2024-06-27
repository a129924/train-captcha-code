from typing import Literal

from pydantic import BaseModel


class CodeList(BaseModel):
    id: int
    code: str
    ans: str


class CaptchaCodeResponse(BaseModel):
    ret: Literal[0]
    codelist: list[CodeList]
