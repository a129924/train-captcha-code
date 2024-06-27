def test_download_pic():
    from src.train_verification_code.service.captcha_code_pic_service import (
        fetch_verification_code_url,
        write_verification_code_pics,
    )

    response_schema = fetch_verification_code_url(
        url="https://gen.caca01.com/ttcode/quest"
    )

    root_path = "./captcha_code_pics"

    for state in write_verification_code_pics(
        root_path=root_path,
        cverification_code_response=response_schema,
    ):
        assert state["state"] == "success"
