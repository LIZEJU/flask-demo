# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/26 10:07 PM
# Project: flask-demo

import  os
import  json
from random import  randint
from faker import Faker
from simpledu.modes import db , User , Course, Chapter

# 创建faker 工厂对象
fake = Faker()

# 生成一个教师用户
def iter_users():
    yield  User(
        username='jack lee',
        email='jacklee@example.com',
        password='111111',
        job='研发工程师',
    )

# 从datas 读取客户才能数据，生成课程数据，将课程教师设置为jack lee

def iter_courses():
    author = User.query.filter_by(username='jack lee').first()
    with open(os.path.join(os.path.dirname(__file__),'..','datas','courses.json')) as f :
        courses = json.load(f)
    for course in courses:
        yield Course(
            name=course['name'],
            description=course['description'],
            image_url=course['image_url'],
            author=author
        )

def iter_chapters():
    for course in Course.query:
        # 每个课程生成2-10 个章节
        for i in range(randint(2,10)):
            yield Chapter(
                # 使用faker 生成一个句子作为章节名称
                name=fake.sentence(),
                course=course,
                # 所有章节的视频设置成了楼+课程中的某个视频
                video_url='https://labfile.oss.aliyuncs.com/courses/923/week2_mp4/2-1-1-mac.mp4',
                # 视频时长
                video_duration='{}:{}'.format(randint(10,30),randint(1,59))
            )

def run():
    for user in iter_users():

        print(user)
        db.session.add(user)
    for course in iter_courses():
        db.session.add(course)
    for chapter in iter_chapters():
        db.session.add(chapter)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

if __name__ == '__main__':
    run()