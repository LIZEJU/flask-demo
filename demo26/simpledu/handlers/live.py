# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/28 3:01 PM
# Project: flask-demo


from flask import Blueprint,render_template , abort
from simpledu.modes import db , Live
live = Blueprint('live',__name__,url_prefix='/live')

@live.route('/lives')
def list():
    try:
        live = Live.query.all()
        return render_template('live/lives.html', lives=live)
    except Exception as e:
        abort(404)

@live.route('/<int:id>')
def get(id):
    live = Live.query.get_or_404(id)
    return render_template('live/index4.html',live=live)