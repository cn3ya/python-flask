from flask import Blueprint
from markupsafe import escape

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
