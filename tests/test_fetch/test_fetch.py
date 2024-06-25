def test_fetch():
    from src.train_verification_code.utils.fetch import fetch_url
    from src.train_verification_code.schema.verification_code_response import (
        VerificationCodeResponse,
    )
    from json import loads

    json_ = loads(fetch_url("https://gen.caca01.com/ttcode/quest"))

    assert VerificationCodeResponse(**json_)
