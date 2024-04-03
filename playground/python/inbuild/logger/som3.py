import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler(filename="pliczek")
logger.addHandler(handler)
