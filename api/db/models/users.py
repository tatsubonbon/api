import time
from datetime import datetime

import jwt
from api.app import db, oauth
from api.db.models.follow import Follow
from flask import current_app, g
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), index=True)
    email = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(100))
    # role_id = db.Column(db.Integer, db.ForeignKey("Role.id"))
    # posts = db.relationship("Post", backref="author", lazy="dynamic")
    # followed = db.relationship(
    #     "Follow",
    #     foreign_keys=[Follow.follower_id],
    #     backref=db.backref("follower", lazy="joined"),
    #     lazy="dynamic",
    #     cascade="all, delete-orphan",
    # )
    # followers = db.relationship(
    #     "Follow",
    #     foreign_keys=[Follow.followed_id],
    #     backref=db.backref("followed", lazy="joined"),
    #     lazy="dynamic",
    #     cascade="all, delete-orphan",
    # )
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            payload={
                "id": self.id,
                "role": self.role_id,
                "exp": time.time() + expires_in,
            },
            key=current_app.config["SECRET_KEY"],
            algorithm="HS256",
        )

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
        except Exception:
            return
        return User.query.get(data["id"])

    def to_dict(self):
        return {"id": self.id, "user_name": self.user_name}


@oauth.verify_password
def verify_password(email_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(email_or_token)
    if not user:
        # try to authenticate with email/password
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
