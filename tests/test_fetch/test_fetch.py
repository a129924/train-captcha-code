def test_fetch():
    from json import loads

    from src.train_verification_code.schema.verification_code_response import (
        VerificationCodeResponse,
    )
    from src.train_verification_code.utils.fetch import fetch_url

    json_ = loads(fetch_url("https://gen.caca01.com/ttcode/quest"))

    assert VerificationCodeResponse(**json_)
