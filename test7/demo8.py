# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 3:27 PM
# Project: test


from flask import Flask , render_template ,abort
# from flask.ext.sqlalchemy import SQLAlchemy
from datetime import  datetime
from flask_sqlalchemy import  SQLAlchemy
from pymongo import MongoClient


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/shiyanlou?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
mongo = MongoClient('127.0.0.1', 27017).shiyanlou
class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('titles',lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self, name,created_time,category,content):
        self.name = name
        if created_time is None:
            created_time = datetime.now()
        self.created_time = created_time
        self.category = category
        self.content = content

    def add_tag(self, tag_name):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            mongo.files.update_one({'file_id': self.id}, {
                '$set': {'tags': tags}})
        else:
            tags = [tag_name]
            mongo.files.insert_one({'file_id': self.id, 'tags': tags})
        return tags

    def remove_tag(self, tag_name):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            try:
                tags.remove(tag_name)
                new_tags = tags
            except ValueError:
                return tags
            mongo.files.update_one({'file_id': self.id}, {
                '$set': {'tags': new_tags}})
            return new_tags
        return []

    @property
    def tags(self):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            return file_item['tags']
        else:
            return []

    def __repr__(self):
        return '<Title %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

def insert_data():
    java = Category('Java')
    python = Category('Python')
    file1 = Title('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = Title('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

    # 增加 MongoDB 中的数据
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')

@app.route('/')
def index():
    data = Title.query.all()


    return  render_template('index.html',data=data)

@app.route('/title/<file_id>')
def file(file_id):
    # file_id 为 File 表中的文章 ID
    # 需要显示 file_id  对应的文章内容、创建时间及类别信息（需要显示类别名称）
    # 如果指定 file_id 的文章不存在，则显示 404 错误页面
    # if  not Title.query.filter_by(id=file_id).first():
    #     abort(404)
    # data = Title.query.filter_by(id=file_id).first()

    data = Title.query.get_or_404(file_id)
    return  render_template('detail.html',file_item=data)

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
    # db.create_all()
    # insert_data()
    '''
    AttributeError: 'datetime.datetime' object has no attribute '_sa_instance_state'
    '''