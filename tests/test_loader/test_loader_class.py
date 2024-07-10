from torch import Tensor


def test_loader_class():
    from src.train_captcha_code.data_set import CaptchaDataSet
    from src.train_captcha_code.loader import CaptchaLoader
    from src.train_captcha_code.project_typing import CaptchaItem

    dataset = CaptchaDataSet(config_path="./config/captcha_data_set.env")
    loader = CaptchaLoader(config_path="./config/train_config.env", dataset=dataset)

    train_loader, val_dataloader = loader.get_loaders()

    for item in train_loader:
        assert isinstance(item, CaptchaItem)
        assert isinstance(item.filepath, Tensor)
        assert isinstance(item.filepath, str)
