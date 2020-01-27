# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/27 3:31 PM
# Project: flask-demo

from flask import  abort
from flask_login import  current_user
from functools import  wraps
from simpledu.modes import User


def role_required(role):
    '''
    带参数的装饰器，可以用它来保护一个路由处理函数智能被特定的用户访问
    :param role:
    :return:
    '''

    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return  func(*args,**kwargs)

        return  wrapper
    return  decorator

# 特定角色的装饰器
staff_required  = role_required(User.ROLE_STAFF)
admin_required  = role_required(User.ROLE_ADMIN)

