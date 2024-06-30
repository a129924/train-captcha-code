from pytest import mark


@mark.asyncio
async def test_500_downloader():
    from src.train_captcha_code.downloader import CaptchaCodeDownloader

    count = 500
    downloader = CaptchaCodeDownloader(
        config_path="./config/download.env",
        target_quantity=count,
        file_extend=".png",
    )

    amount = 0

    states = await downloader.pipeline()

    if states:
        for state in states:
            amount += 1

            assert state["state"] == "success"

        assert amount >= count

    # assert downloader.remaining_quantity == 0
    # assert downloader.config == ""
    # assert states is not None
