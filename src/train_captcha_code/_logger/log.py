def create_logger(
    logger_name: str = __name__,
    *,
    logger_path: str,
):
    from logging import FileHandler, Formatter, getLogger

    logger = getLogger(logger_name)
    handler = FileHandler(filename=logger_path, encoding="UTF-8")
    handler.setFormatter(Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S"))

    logger.addHandler(handler)
    logger.setLevel(20)

    return logger
