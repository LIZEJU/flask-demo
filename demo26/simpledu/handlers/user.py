from flask import Blueprint , render_template ,abort
from simpledu.modes import User
users = Blueprint('user',__name__,url_prefix='/user')



@users.route('/<username>')
def user(username):
    user_info = User.query.filter(User.username==username).first()
    if user_info is None:
        abort(404)
    return render_template('user_info.html', user_info=user_info)

@users.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404