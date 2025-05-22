import logging
import requests
import requests
import warnings


logging.basicConfig(level=logging.DEBUG)
# logging.getLogger("requests").setLevel(logging.INFO)
# logging.basicConfig()


# requests.get("https://google.com")


class CustomHandler(logging.Handler):
    def emit(self, record):
        print("ABC")
        # return 1


class CustomFormatter(logging.Formatter):
    # def formatMessage(self, record) -> dict:
    #     """
    #     Overwritten to return a dictionary of the relevant LogRecord attributes instead of a string.
    #     KeyError is raised if an unknown attribute is provided in the fmt_dict.
    #     """
    #     return {fmt_key: record.__dict__[fmt_val] for fmt_key, fmt_val in self.fmt_dict.items()}

    def format(self, record: logging.LogRecord):
        # print(record.__dict__)
        # record.msg = "ABC"
        msg = super().format(record)
        # print(msg)
        return msg

        # return "ABC"


class NoParsingFilter(logging.Filter):
    def filter(self, record):
        return True
        # return not record.getMessage().startswith("parsing")


# return "ABC"

logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig()
# logging.lastResort = False

# logging.lastResort = False
logger = logging.getLogger(__name__)
logger.propagate = False
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter("%(levelname).3s A %(asctime)s"))
logger.addHandler(handler)
logger.addHandler(CustomHandler())
logger.propagate = True
# logger.addFilter(NoParsingFilter())
logger.warning("A")
# logging.info("A")
# warnings.warn("CO JEST")


# custom_format = {
#     "level": "%(levelname)s",
#     "where": "%(name)s",
#     "when": "%(asctime)s",
# }
