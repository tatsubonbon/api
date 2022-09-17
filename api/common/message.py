from typing import Union

message_dict = {
    "CM0000I": "必須なパラメータがありません：{name}",
    "CM0001I": "{name}に成功しました。",
    "CM0002E": "{name}に失敗しました。",
    "CM0003I": "{name}はすでに存在します。",
    "CM0004I": "test",
    "CM0005I": "test",
    "CM0006E": "{name}が見つかりません。",
    "CM0007I": "test",
    "CM0008I": "test",
}


def get_message(message_id: str, **kwarg: Union[str, int]) -> str:
    """
    メッセージIDに対応するメッセージを取得する。

    Parameters
    ----------
    message_id : str
        message_dictに定義してあるメッセージID。
    kwarg : Union[str, int]
        メッセージに変数の値をフォーマットする辞書。

    Returns
    -------
    メッセージIDに対応するメッセージ : str
    """
    try:
        msg = f"{message_dict[message_id]}"
        return msg.format(**kwarg)
    except Exception:
        raise
