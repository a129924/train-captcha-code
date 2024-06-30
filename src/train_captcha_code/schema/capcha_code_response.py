from typing import Literal

from pydantic import BaseModel


class CodeList(BaseModel):
    id: int
    code: str
    ans: str

    def __hash__(self):
        return hash((self.code, self.ans))


class CaptchaCodeResponse(BaseModel):
    ret: Literal[0]
    codelist: list[CodeList]
