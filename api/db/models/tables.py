import time
from datetime import datetime

import jwt
from api.app import db, oauth
from flask import current_app, g
from werkzeug.security import check_password_hash, generate_password_hash


class Follow(db.Model):
    __tablename__ = "follows"
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.String(100), primary_key=True)
    post_id = db.Column(db.String(100), db.ForeignKey("posts.id"))
    image_path = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(100))
    text = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship("User", backref="role", lazy="dynamic")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), index=True)
    email = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(100))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    followed = db.relationship(
        "Follow",
        foreign_keys=[Follow.follower_id],
        backref=db.backref("follower", lazy="joined"),
        lazy="dynamic",
        cascade="all, delete-orphan",
    )
    followers = db.relationship(
        "Follow",
        foreign_keys=[Follow.followed_id],
        backref=db.backref("followed", lazy="joined"),
        lazy="dynamic",
        cascade="all, delete-orphan",
    )
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
    # トークンで認証
    user = User.verify_auth_token(email_or_token)
    print(user)
    print(email_or_token)
    if not user:
        # email/passwordで認証
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
