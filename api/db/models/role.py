from datetime import datetime

from api.app import db, ma


class Permission:
    FOLLOW = 1
    COMMENT = 2
    POST = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    __tablename__ = "Role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship("User", backref="role", lazy="dynamic")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role

    id = ma.auto_field()
    name = ma.auto_field()
    default = ma.auto_field()
    permissions = ma.auto_field()
    users = ma.auto_field()
