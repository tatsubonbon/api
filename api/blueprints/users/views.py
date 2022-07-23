from api.app import db, oauth
from api.blueprints.models import User
from flask import Blueprint, jsonify, request, url_for

user_blueprint = Blueprint("users", __name__, url_prefix="/v1/users")


@user_blueprint.route("/", methods=["GET"])
@oauth.login_required
def get_users():
    try:
        from sqlalchemy.exc import SQLAlchemyError

        users = User.query.all()

        return jsonify({"users": [user.to_dict() for user in users]}), 200
    except SQLAlchemyError:
        return jsonify({"message": "Fail get users"}), 400


@user_blueprint.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        from sqlalchemy.exc import SQLAlchemyError

        user = User.query.filter_by(id=user_id).first()

        if user:
            return jsonify({"user": user.to_dict()}), 200
        return jsonify({"message": "No user"}), 400
    except SQLAlchemyError:
        return jsonify({"message": "Fail get user"}), 400


@user_blueprint.route("/", methods=["POST"])
def create_user():
    # jsonリクエストから値取得
    payload = request.json
    username = payload.get("username")
    email = payload.get("email")
    password = payload.get("password")

    if username is None or password is None:
        return jsonify({"message": "Username or password is empty"}), 400
    try:
        from sqlalchemy.exc import IntegrityError, SQLAlchemyError

        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        return (
            jsonify({"username": user.username}),
            201,
            {"Location": url_for("users.get_user", user_id=user.id, _external=True)},
        )
    except IntegrityError:
        # メールアドレス重複登録
        return jsonify({"message": f"Already existing email: {email}"}), 409
    except SQLAlchemyError:
        return jsonify({"message": f"Fail create user: {username}"}), 400


@user_blueprint.route("/<user_id>", methods=["DELETE"])
@oauth.login_required
def delete_user(user_id):
    try:
        from sqlalchemy.exc import SQLAlchemyError

        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "Success delete user"}), 200
    except SQLAlchemyError:
        return jsonify({"message": "Fail delete user"}), 400
