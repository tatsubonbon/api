import os


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    OAUTH2_REFRESH_TOKEN_GENERATOR = True
    LOG_PATH = ""
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "consoleFormatter": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            },
            "logFileFormatter": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "formatter": "consoleFormatter",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "backupCount": 3,
                "formatter": "logFileFormatter",
                "mode": "w",
                "filename": "./app.log",
                "encoding": "utf-8",
            },
        },
        "loggers": {"basic": {"handlers": ["file", "console"], "level": "DEBUG"}},
        "root": {"level": "DEBUG", "handlers": ["file", "console"]},
    }
