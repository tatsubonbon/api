import os


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    OAUTH2_REFRESH_TOKEN_GENERATOR = True
