def test_fetch():
    from src.train_verification_code.schema.verification_code_response import (
        VerificationCodeResponse,
    )
    from src.train_verification_code.utils.sync.fetch import fetch_url_to_json

    json_ = fetch_url_to_json("https://gen.caca01.com/ttcode/quest")

    assert VerificationCodeResponse(**json_)
