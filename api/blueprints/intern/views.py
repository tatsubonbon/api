from flask import Blueprint, jsonify, request, url_for

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
