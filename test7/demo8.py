# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 3:27 PM
# Project: test


from flask import Flask , render_template ,abort
# from flask.ext.sqlalchemy import SQLAlchemy
from datetime import  datetime
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/shiyanlou?charset=utf8'
db = SQLAlchemy(app)

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('titles',lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self, name,category,content,created_time=None):
        self.name = name
        if created_time is None:
            created_time = datetime.now()
        self.created_time = created_time
        self.category = category
        self.content = content


    def __repr__(self):
        return '<Title %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

@app.route('/')
def index():
    data = Title.query.all()


    return  render_template('index.html',data=data)

@app.route('/title/<file_id>')
def file(file_id):
    # file_id 为 File 表中的文章 ID
    # 需要显示 file_id  对应的文章内容、创建时间及类别信息（需要显示类别名称）
    # 如果指定 file_id 的文章不存在，则显示 404 错误页面
    if  not Title.query.filter_by(id=file_id).first():
        abort(404)
    data = Title.query.filter_by(id=file_id).first()
    return  render_template('detail.html',t=data)

@app.route('/cate/<file_id>')
def cate(file_id):
    # file_id 为 File 表中的文章 ID
    # 需要显示 file_id  对应的文章内容、创建时间及类别信息（需要显示类别名称）
    # 如果指定 file_id 的文章不存在，则显示 404 错误页面
    if  not Category.query.filter_by(id=file_id).first():
        abort(404)
    cate = Category.query.filter_by(id=file_id).first()
    data = cate.titles.all()
    print(data)
    return  render_template('cate.html',t=data)

@app.errorhandler(404)
def error_404(error):
    return  render_template('404.html'),404
if __name__ == '__main__':
    app.run(debug=True)

    '''
    AttributeError: 'datetime.datetime' object has no attribute '_sa_instance_state'
    '''