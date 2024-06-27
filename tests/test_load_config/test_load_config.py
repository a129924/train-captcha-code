def test_load_config():
    from dotenv import dotenv_values

    from src.train_captcha_code.config.download import DownloadConfig

    config_path = "./config/download.env"

    pydantic_config = DownloadConfig.set_model_config(
        {"env_file": "./config/download.env", "env_file_encoding": "UTF-8"}
    )().model_dump()  # type: ignore

    assert dict(dotenv_values(config_path)) == pydantic_config
