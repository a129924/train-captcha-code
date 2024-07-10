from .log import create_logger  # noqa: F403

__all__ = ["Logger"]

Logger = create_logger(logger_path="./log/.log")
