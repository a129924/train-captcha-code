def test_check_ratio_config():
    from src.train_captcha_code.config.train_config import TrainConfig

    config = TrainConfig.set_model_config(
        model_config={
            "env_file": "./config/train_config.env",
            "env_file_encoding": "UTF-8",
        }
    )()  # type: ignore

    assert config
