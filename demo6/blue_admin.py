#encoding:utf-8

from flask import  Blueprint,request

bp = Blueprint('admin_bp',__name__,subdomain='admin')

@bp.route('/')
def get_cookie():
    username = request.cookies.get('username')

    return  username or "没有获取到name值"
