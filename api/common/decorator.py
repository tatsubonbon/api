from functools import wraps
from logging import Logger


def logging_api(logger: Logger):
    """
    APIの開始、終了のログを出力します
    """

    def _decorator(func):

        # funcのメタデータを引き継ぐ
        @wraps(func)
        def wrapper(*args, **kwargs):

            func_name = func.__name__

            try:
                logger.info(f"{func_name}開始")
                # funcの実行
                return func(*args, **kwargs)
            finally:
                logger.info(f"{func_name}終了")

        return wrapper

    return _decorator
