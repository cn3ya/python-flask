from flask import Blueprint

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route("/me")
def me_api():
    return {
        "username": 'user.username',
        "theme": 'user.theme',
        "image": 'url_for("user_image", filename=user.image)',
    }
