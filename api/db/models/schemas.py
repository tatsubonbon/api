from api.app import ma
from api.db.models.tables import Follow, Image, Post, Role


class FollowSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Follow

    follower_id = ma.auto_field()
    followed_id = ma.auto_field()


class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Image

    id = ma.auto_field()
    post_id = ma.auto_field()
    image_path = ma.auto_field()


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

    id = ma.auto_field()
    user_id = ma.auto_field()
    title = ma.auto_field()
    text = ma.auto_field()


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role

    id = ma.auto_field()
    name = ma.auto_field()
    default = ma.auto_field()
    permissions = ma.auto_field()
    users = ma.auto_field()
