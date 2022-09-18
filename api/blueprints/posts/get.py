from api.app import oauth
from api.blueprints.posts import blueprint
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.columns.postsCol import PostColumns
from api.db.models.schemas import ImageSchema, PostSchema
from api.db.models.tables import Image, Post
from sqlalchemy.exc import SQLAlchemyError


@blueprint.route("/<post_id>", methods=["GET"])
@oauth.login_required
def get_post(post_id):
    try:

        post = Post.query.filter_by(id=post_id).first()
        post = PostSchema().dump(post)

        images = Image.query.filter_by(post_id=post[PostColumns.ID]).first()
        images = ImageSchema().dump(images)

        image_path = Path(images["image_path"])

        with open(image_path, mode="r") as f:
            data = f.read()
        return make_response(
            get_message("CM0006E", name="ユーザー"), StatusCode.SUCCCESS, data
        )
    except IOError:
        return make_error_response(
            get_message("CM0002E", name="投稿の取得"), StatusCode.ERROR
        )
    except SQLAlchemyError:
        return make_error_response(
            get_message("CM0002E", name="投稿の取得"), StatusCode.ERROR
        )
    except Exception:
        return make_error_response(
            get_message("CM0002E", name="投稿の取得"), StatusCode.ERROR
        )
