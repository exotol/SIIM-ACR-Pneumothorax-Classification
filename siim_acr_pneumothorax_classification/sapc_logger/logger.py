import yaml
import logging
import logging.config
from typing import Text


def logger_factory(logger_name: Text) -> logging.Logger:
    with open("configs/loggers.yaml", "r", encoding="utf-8") as cfg:
        cfg_log = yaml.safe_load(cfg.read())
        logging.config.dictConfig(cfg_log)

    return logging.getLogger(logger_name)

