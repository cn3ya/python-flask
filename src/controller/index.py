from flask import Blueprint

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return 'Index Page'

@bp.route('/hello')
def hello():
    return 'Hello, World'

@bp.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@bp.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
