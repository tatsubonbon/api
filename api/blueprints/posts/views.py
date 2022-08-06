import os
import uuid
from pathlib import Path

from api.app import db
from api.blueprints.models import Image, Post, User
from flask import Blueprint, current_app, jsonify, request

post_blueprint = Blueprint("posts", __name__, url_prefix="/v1/posts")


@post_blueprint.route("/", methods=["POST"])
def set_post():
    try:
        from sqlalchemy.exc import SQLAlchemyError

        payload = request.json
        post_id = uuid.uuid4()
        user_id = payload.get("user_id")
        title = payload.get("title")
        text = payload.get("text")
        images = payload.get("images")

        if user_id is None or title is None or text is None:
            return jsonify({"message": "user_id or title or text is empty"}), 400

        post = Post(id=str(post_id), user_id=int(user_id), title=title, text=text)
        db.session.add(post)
        db.session.commit()

        image_path = Path(current_app.config["UPLOAD_DIR"] + str(user_id))
        if not os.path.isdir(image_path):
            os.mkdir(image_path)

        if images:
            for image in images:
                id = str(uuid.uuid4())
                file = open(f"{image_path}/{id}.txt", "w")
                file.write(image)
                file.close()
                image = Image(
                    id=id, post_id=str(post_id), image_path=f"{image_path}/{id}.txt"
                )
                db.session.add(image)
                db.session.commit()

        return jsonify({"message": "Success register posts"}), 201
    except IOError:
        return jsonify({"message": "Fail register posts"}), 400
    except SQLAlchemyError as e:
        print(e)
        return jsonify({"message": "Fail register posts"}), 400
