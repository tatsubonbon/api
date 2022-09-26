from api.blueprints.oauth import get as get_oauth
from api.blueprints.posts import delete as delete_posts
from api.blueprints.posts import get as get_posts
from api.blueprints.posts import post as post_posts
from api.blueprints.posts import put as put_posts
from api.blueprints.users import delete as delete_user
from api.blueprints.users import get as get_user
from api.blueprints.users import post as post_user
from api.blueprints.users import put as put_user

blueprints_list = [
    get_oauth,
    get_posts,
    post_posts,
    put_posts,
    delete_posts,
    delete_user,
    get_user,
    post_user,
    put_user,
]
