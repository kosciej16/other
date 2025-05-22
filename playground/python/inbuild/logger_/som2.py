import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger = logging.getLogger(__name__)
logger.warning("A")
logging.warning("A")
logger.warning("A")
