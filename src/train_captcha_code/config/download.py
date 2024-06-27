from .base import BaseConfig


class DownloadConfig(BaseConfig):
    root_path: str
    captcha_code_pic_path: str
    captcha_code_pic_url: str
