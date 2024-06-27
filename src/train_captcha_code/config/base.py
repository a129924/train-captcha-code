from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self

__all__ = ["BaseConfig"]


class BaseConfig(BaseSettings):
    @classmethod
    def set_model_config(cls, model_config: SettingsConfigDict) -> type[Self]:
        cls.model_config = model_config

        return cls
