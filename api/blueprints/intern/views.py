import json
from pathlib import Path

import pandas as pd
from api.blueprints.intern.syazyounerai_columns import (
    SyazyouneraiData,
    SyazyouneraiDataAdd,
)
from flask import Blueprint, current_app, jsonify, request

intern_blueprint = Blueprint("intern", __name__, url_prefix="/v1/intern")

# http://127.0.0.1:5000/v1/intern/
# GETメソッド
@intern_blueprint.route("/", methods=["GET"])
def get_test():
    tests = [1, 2, 3, "a", "b"]
    return jsonify({"test": [test for test in tests]}), 200


# http://127.0.0.1:5000/v1/intern/request
# POSTメソッド
@intern_blueprint.route("/request", methods=["POST"])
def get_request_test():
    # json取得
    # {"test": "..."}を受けるとする
    req = request.json
    test = req.get("test")
    return jsonify({"test": "{format}を受け取りました".format(format=test)}), 200


# http://127.0.0.1:5000/v1/intern/syazyounerai
# GETメソッド
@intern_blueprint.route("/syazyounerai", methods=["GET"])
def get_syazyounerai():
    try:
        input_file = Path(current_app.config["DATA_DIR"] + "tokyo_2021syazyounerai.csv")
        df = pd.read_csv(
            input_file,
            usecols=SyazyouneraiData.columns,
            dtype=SyazyouneraiData.dtypes,
            encoding="Shift-jis",
        )
        # 管轄警察署（発生地）ごとの数を追加する
        police_station_count = df.groupby((SyazyouneraiData.POLICE_STATION_AREA)).size()
        pd.options.display.max_rows = 100
        return {"result": {police_station_count.idxmax(): police_station_count.max()}}
    except Exception as e:
        print(e)
        return jsonify({"message": "Fail get syazyounerai"}), 400
