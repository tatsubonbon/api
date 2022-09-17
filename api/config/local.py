import os
from pathlib import Path

from api.config.base import BaseConfig

base_dir = Path(__file__).parent.parent


MYSQL = os.getenv("MYSQL")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB_NAME = os.getenv("MYSQL_DB_NAME")


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"{MYSQL}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    UPLOAD_DIR = f"{base_dir}/images/"
