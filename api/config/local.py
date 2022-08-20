from pathlib import Path

from api.config.base import BaseConfig

base_dir = Path(__file__).parent.parent


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    UPLOAD_DIR = f"{base_dir}/images/"
    DATA_DIR = f"{base_dir}/datas/"
