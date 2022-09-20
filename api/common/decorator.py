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

            logger.info(f"[{func_name}開始")

            try:
                # funcの実行
                return func(*args, **kwargs)
            except Exception as err:
                # funcのエラーハンドリング
                logger.error(err, exc_info=True)
                logger.error(f"{func_name}異常が発生しました")
            finally:
                logger.info(f"{func_name}終了")

        return wrapper

    return _decorator
