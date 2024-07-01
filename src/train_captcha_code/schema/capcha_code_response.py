from typing import Literal

from pydantic import BaseModel


class CodeList(BaseModel):
    id: int
    code: str
    ans: str

    def __hash__(self) -> int:
        return hash((self.ans, self.code))


class CaptchaCodeResponse(BaseModel):
    ret: Literal[0]
    codelist: list[CodeList]
