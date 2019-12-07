#encoding:utf-8

# 引入form基类
from flask_wtf import Form
# 引入form元素父类
from wtforms import  StringField , PasswordField ,FileField
# 引入form验证父类
from wtforms.validators import  DataRequired,Length
from wtforms.validators import InputRequired
from flask_wtf.file import  FileRequired , FileAllowed
from flask_wtf.form import FlaskForm
# 登录表单类，继承form类
class BaseLogin(Form):
    # 用户名
    name = StringField('name',validators=[DataRequired(message='用户名不能为空'),Length(6,16,message='长度位于6-16之间')],render_kw={'placeholder':'输入用户名'})
    password = PasswordField('password',validators=[DataRequired(message='密码不能为空'),Length(6,16,message='长度位于6-16之间')],render_kw={'placeholder':'输入密码'})


from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(Form):
    file = FileField(validators=[FileRequired(),  # FileRequired必须上传
                                 FileAllowed(['jpg', 'png', 'gif'])  # FileAllowed:必须为指定的格式的文件
                                 ])
