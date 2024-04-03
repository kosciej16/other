import logging
import requests

# logging.getLogger("sqlalchemy.engine").setLevel("DEBUG")

logging.basicConfig()
logging.getLogger().setLevel(0)
logging.getLogger("urllib3").setLevel("INFO")
requests.get("https://www.google.com")


# class MyHandler(logging.Handler):
#     def emit(self, record: logging.LogRecord):
#         print("JESTEM")


# class MyFormatter(logging.Formatter):
#     def format(self, record: logging.LogRecord):
#         return "ABC"


# class MyFilter(logging.Filter):
#     def filter(self, record: logging.LogRecord):
#         return not record.getMessage().startswith("abc")


# # logging.basicConfig()
# # logging.getLogger()
# # logging.getLogger().setLevel(logging.DEBUG)
# # logging.info("A")

# # 1

logger = logging.getLogger(__name__)
# logging.getLogger("abc")
# logging.getLogger("abc.def")
# # handler = MyHandler()
# handler = logging.StreamHandler()
# formatter = MyFormatter()
# handler.setFormatter(formatter)

# # logging.lastResort = False
# # logger.setLevel(logging.DEBUG)

# # default
# logger.propagate = False

# logger.addHandler(handler)
# handler2 = logging.StreamHandler()
# formatter = logging.Formatter("%(levelname).3s: %(msg)s %(lineno)s")
# handler2.setFormatter(formatter)
# logger.addHandler(handler2)
# logger.addFilter(MyFilter())
# logging.basicConfig()
# logger.warning("abc xyz")
# # logging.warning("A")
# # logger.warning("A")

# # logger.setLevel(10)
# # logger.setLevel("DEBUG")
# # logger2 = logging.getLogger("ABC")

# # print(logger is logger2)
# # logger.info("A")
# # # 2
# # logging.info("A")
