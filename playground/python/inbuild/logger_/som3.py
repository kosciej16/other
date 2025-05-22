import logging
from pathlib import Path


logger = logging.getLogger(__name__)


def l():
    logger = logging.getLogger(__name__)
    path = Path("sciezka/pliczek")
    path.parent.mkdir(parents=True, exist_ok=True)
    f_handler = logging.FileHandler(path)

    handler = logging.FileHandler(filename=path)
    logger.addHandler(handler)


l()
logger.warning("DUPA")
