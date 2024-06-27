from pytest import mark


@mark.asyncio
async def test_500_downloader():
    from src.train_captcha_code.downloader import CaptchaCodeDownloader

    count = 500
    downloader = CaptchaCodeDownloader(
        config_path="./config/download.env",
        limit_file_count=count,
    )

    amount = 0

    async for states in downloader.pipeline():
        for state in states:
            amount += 1

            assert state["state"] == "success"

    assert amount >= count
