from dataclasses import dataclass
import logging

from strlog import configure_structlog

@dataclass()
class Config:
    log_path: str = "/home/kosciej/logs/"
    log_level: str = "DEBUG"

c = Config()

logger = configure_structlog(c)

logger = logger.bind(zmienna="X")
logger.info("ABC", a="WAR")

lg = logging.getLogger("eml_shooter")
lg.info("X")
