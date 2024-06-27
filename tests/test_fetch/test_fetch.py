def test_fetch():
    from train_captcha_code.schema.capcha_code_response import (
        CaptchaCodeResponse,
    )

    from src.train_captcha_code.utils.sync.fetch import fetch_url_to_json

    json_ = fetch_url_to_json("https://gen.caca01.com/ttcode/quest")

    assert CaptchaCodeResponse(**json_)
