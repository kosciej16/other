import structlog
import logging
import os

level = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, level)
structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(LOG_LEVEL))
# logger = structlog.get_logger()
logger = logging.getLogger(__name__)

logger.debug("Database connection established")
logger.info("Processing data from the API")
logger.warning("Resource usage is nearing capacity")
logger.error("Failed to save the file. Please check permissions")
logger.critical("System has encountered a critical failure. Shutting down")
