from api.app import db, ma
from api.blueprints.users import user_blueprint
from api.common.message import get_message
from api.common.setting import StatusCode
from api.db.models.users import User
from flask import jsonify, request, url_for
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class RequestSchema(ma.Schema):
    user_name = ma.String(required=True)
    email = ma.Email(required=True)
    password = ma.String(required=True)
    # role_id = ma.Integer(required=True)


@user_blueprint.route("/", methods=["POST"])
def create_user():
    try:
        requestSchema = RequestSchema()
        payload = requestSchema.load(request.json)
    except Exception as e:
        print(e)

        return (
            jsonify({"message": get_message("CM0000I", name="test")}),
            StatusCode.ERROR,
        )

    try:
        user_name = payload.get("user_name")
        email = payload.get("email")
        password = payload.get("password")

        user = User(user_name=user_name, email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        return (
            jsonify({"user_name": user.user_name}),
            StatusCode.POST_SUCCESS,
            {"Location": url_for("users.get_user", user_id=user.id, _external=True)},
        )
    except IntegrityError:
        # メールアドレス重複登録
        return (
            jsonify({"message": get_message("CM0003I", name="そのemail")}),
            StatusCode.DUPLICATION_ERROR,
        )
    except SQLAlchemyError as e:
        print(e)
        return (
            jsonify({"message": get_message("CM0002E", name="ユーザー登録")}),
            StatusCode.ERROR,
        )
