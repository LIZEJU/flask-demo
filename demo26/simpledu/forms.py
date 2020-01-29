from flask_wtf import  FlaskForm
from wtforms import  StringField , PasswordField, SubmitField , BooleanField ,ValidationError ,TextAreaField ,IntegerField,SelectField
from wtforms.validators import  Length , Email, EqualTo , DataRequired ,URL ,NumberRange,AnyOf
from simpledu.modes import  User  ,db ,Course , Live
from flask import  flash
import re

class RegisterForm(FlaskForm):

    username = StringField('用户名',validators=[DataRequired(),Length(3,24)])
    email = StringField('邮箱',validators=[DataRequired(),Email(message='请输入合法的email地址')])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24,message='密码长度时6位到24位')])
    repeat_password = PasswordField('重复密码',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return  user

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise  ValidationError('用户名已经存在')
        username = field.data
        pattern = re.compile('\w+\d+')
        s = pattern.search(username).group(0)
        if  len(s) != len(username):
            flash('用户名只能是数字和字母')
            raise ValidationError('')


    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')



class LoginForm(FlaskForm):
    # email = StringField('邮箱', validators=[DataRequired(), Email(message='邮箱格式错误')])
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24,message='密码长度时6位到24位')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_username(self,field):

        if not User.query.filter_by(username=field.data).first():
            raise  ValidationError('用户未注册')

    def validate_password(self,field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise  ValidationError('密码错误')


class CourseForm(FlaskForm):
    name = StringField('课程名称',validators=[DataRequired(),Length(5,20)])
    description = TextAreaField('课程简介',validators=[DataRequired(),Length(20,256)])
    image_url = StringField('封面图片',validators=[DataRequired(),URL()])
    author_id = IntegerField('作者id',validators=[DataRequired(),NumberRange(min=1,message='无效的用户的id')])
    submit = SubmitField('提交')

    def validate_author_id(self,field):
        if not User.query.filter_by(id=field.data).first():
            raise  ValidationError('用户不存在')

    def create_course(self):
        course = Course()
        # 使用课程表单数据填充course对象
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self,course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

class UserForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    role = SelectField('角色', validators=[DataRequired()],choices=[(10,'普通用户'),(20,'客服人员'),(30,'管理人员')],default = 10,coerce=int)
    job = StringField('工作', validators=[DataRequired(),Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24, message='密码长度时6位到24位')])

    submit = SubmitField('提交')

    def validate_username(self,field):
        if  User.query.filter_by(username=field.data).first():
            raise  ValidationError('用户已经存在，不能创建')

    def create_user(self):
        user = User()
        # 使用课程表单数据填充course对象
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self,user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user


class UserForm1(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    role = SelectField('角色', validators=[DataRequired()],choices=[(10,'普通用户'),(20,'客服人员'),(30,'管理人员')],default = 10,coerce=int)
    job = StringField('工作', validators=[DataRequired(),Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24, message='密码长度时6位到24位')])

    submit = SubmitField('提交')

    def update_user(self,user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user


class LiveForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired(), Length(3, 24)])
    description = StringField('直播简介', validators=[DataRequired(), Length(3, 24)])

    # chapter_id = IntegerField('章节', validators=[DataRequired(), NumberRange(min=1, message='无效的用户的id')],default=1)

    # chapter_id = SelectField('章节', validators=[DataRequired()], choices=Live.chapters,
    #                    default=Live.chapters[0], coerce=int)
    submit = SubmitField('提交')


    # def validate_chapter_id(self,field):
    #     if   Live.query.filter_by(chapter_id=field.data).first():
    #         raise  ValidationError('章节id不存在')
    def create_live(self):
        live = Live()
        # 使用课程表单数据填充course对象
        self.populate_obj(live)
        db.session.add(live)
        db.session.commit()
        return live

