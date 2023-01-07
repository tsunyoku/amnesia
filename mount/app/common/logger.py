import logging

import structlog

logger = structlog.get_logger()


def init_logging(log_level: str | int) -> None:
    logging.basicConfig(level=log_level)
    info("Logging initialized")


def debug(*args, **kwargs) -> None:
    return logger.debug(*args, **kwargs)


def info(*args, **kwargs) -> None:
    return logger.info(*args, **kwargs)


def warning(*args, **kwargs) -> None:
    return logger.warning(*args, **kwargs)


def error(*args, **kwargs) -> None:
    return logger.error(*args, **kwargs)


def critical(*args, **kwargs) -> None:
    return logger.critical(*args, **kwargs)
