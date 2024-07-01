def test_train_loader():
    from src.train_captcha_code.config.train_config import TrainConfig
    from src.train_captcha_code.data_set import CaptchaDataSet
    from src.train_captcha_code.utils.model import (
        create_loader,
        get_train_size_and_test_size,
        split_data_set,
    )

    dataset = CaptchaDataSet("./config/captcha_data_set.env")
    config = TrainConfig.set_model_config(
        {
            "env_file": "./config/train_config.env",
            "env_file_encoding": "UTF-8",
        }
    )()  # type: ignore

    train_dataset, test_dataset = split_data_set(
        data_set=dataset,
        split_sizes=get_train_size_and_test_size(config.train_ratio, len(dataset)),
    )
    train_loader = create_loader(
        data_set=train_dataset, batch_size=config.batch_size, shuffle=True
    )
    test_loader = create_loader(
        data_set=test_dataset, batch_size=config.batch_size, shuffle=False
    )

    assert train_loader, test_loader
