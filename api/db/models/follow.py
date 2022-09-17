from datetime import datetime

from api.app import db, ma


class Follow(db.Model):
    __tablename__ = "Follow"
    follower_id = db.Column(db.Integer, db.ForeignKey("Users.id"), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey("Users.id"), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class FollowSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Follow

    follower_id = ma.auto_field()
    followed_id = ma.auto_field()
