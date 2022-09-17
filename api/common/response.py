from typing import Any

from api.common.setting import StatusCode
from flask import jsonify

MESSAGE = "message"
RESULT = "result"
STATUS_CODE = "code"


def make_response(message: str, status_code: StatusCode, data: Any):
    """
    クライアントにリスポンスを返却します。

    Parameters
    ----------
    message : str
        クライアントに表示するメッセージ。
    status_code : StatusCode
        HTTPステータスコード。
    data : Any
        クライアントに返却するデータ。

    Returns
    -------
    クライアントに返却するリスポンス : JSON
    """
    return (
        jsonify({MESSAGE: message, STATUS_CODE: status_code, RESULT: data}),
        status_code,
    )


def make_error_response(message: str, status_code: StatusCode):
    """
    クライアントにエラーリスポンスを返却します。

    Parameters
    ----------
    message : str
        クライアントに表示するメッセージ。
    status_code : StatusCode
        HTTPステータスコード。

    Returns
    -------
    クライアントに返却するリスポンス : JSON
    """
    return (
        jsonify({MESSAGE: message, STATUS_CODE: status_code}),
        status_code,
    )
