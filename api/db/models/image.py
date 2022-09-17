from datetime import datetime

from api.app import db, ma


class Image(db.Model):
    __tablename__ = "Image"

    id = db.Column(db.String(100), primary_key=True)
    post_id = db.Column(db.String(100), db.ForeignKey("Posts.id"))
    image_path = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Image

    id = ma.auto_field()
    post_id = ma.auto_field()
    image_path = ma.auto_field()
