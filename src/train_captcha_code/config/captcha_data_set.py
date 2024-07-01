from .base import BaseConfig


class CaptchaDatasetConfig(BaseConfig):
    captcha_code_pic_path: str
    target_file_extension: str
