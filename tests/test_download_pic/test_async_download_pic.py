from pytest import mark


@mark.asyncio
async def test_async_download_pic():
    from asyncio import gather

    from src.train_captcha_code.service.captcha_code_pic_service import (  # type: ignore
        async_write_verification_code_pic,
        fetch_verification_code_url,
    )

    response_schema = fetch_verification_code_url(
        url="https://gen.caca01.com/ttcode/quest"
    )
    root_path = "./captcha_code_pics"

    states = await gather(
        *[
            async_write_verification_code_pic(
                root_path=root_path,
                text=codelist.code,
                filename=f"{codelist.ans}.png",
            )
            for codelist in response_schema.codelist
        ]
    )

    for state in states:
        assert state["state"] == "success"
