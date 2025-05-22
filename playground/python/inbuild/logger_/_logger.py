import logging
import logging.handlers


class CustomHandler(logging.handlers.RotatingFileHandler):
    def emit(self, record):
        self.doRollover()
        super().emit(record)


class SimpleHandler(logging.Handler):
    def emit(self, record):
        a = getattr(record, "test", None)
        print(a)
        setattr(record, "test", "cos")
        return 1


def rotate_every_log():
    LOG_FILENAME = "logging_rotatingfile_example.out"

    logger = logging.getLogger("MyLogger")
    logger.addHandler(CustomHandler(LOG_FILENAME, backupCount=50))
    logger.setLevel(logging.DEBUG)

    logger.info("I'm written to my own file")
    logger.info("I'm written to my own file #2")
    logger.info("I'm written to my own file #3")


class NoParsingFilter(logging.Filter):
    def filter(self, record):
        print("FILTER")
        return not record.getMessage().startswith("parsing")


def filters():
    root_logger = logging.getLogger()

    # logger = logging.getLogger("module_name")

    handler = SimpleHandler()
    handler.addFilter(NoParsingFilter())
    root_logger.addHandler(handler)
    root_logger.addHandler(SimpleHandler())
    # logger = logging.getLogger("NAZWA")


filters()
logging.error("HA")
