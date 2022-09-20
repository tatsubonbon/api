from logging.config import dictConfig


def init_log():
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "root": {
                "level": "DEBUG",
                "handlers": ["consoleHandler", "logFileHandler"],
            },
            "handlers": {
                "consoleHandler": {
                    "class": "logging.StreamHandler",
                    "level": "INFO",
                    "formatter": "consoleFormatter",
                    "stream": "ext://sys.stdout",
                },
                "logFileHandler": {
                    "class": "logging.FileHandler",
                    "level": "DEBUG",
                    "formatter": "logFileFormatter",
                    "filename": "./app.log",
                    "mode": "w",
                    "encoding": "utf-8",
                },
            },
            "formatters": {
                "consoleFormatter": {
                    "format": "[%(levelname)-8s]%(funcName)s - %(message)s"
                },
                "logFileFormatter": {
                    "format": "%(asctime)s|%(levelname)-8s|%(name)s|%(funcName)s|%(message)s"
                },
            },
        }
    )
