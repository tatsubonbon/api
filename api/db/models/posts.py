from datetime import datetime

from api.app import db, ma


class Post(db.Model):
    __tablename__ = "Posts"

    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    title = db.Column(db.String(100))
    text = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

    id = ma.auto_field()
    user_id = ma.auto_field()
    title = ma.auto_field()
    text = ma.auto_field()
