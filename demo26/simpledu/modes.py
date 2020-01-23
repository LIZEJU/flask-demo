from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import  generate_password_hash , check_password_hash
# 注意这里不再传入 app 了
db = SQLAlchemy()

class  Base(db.Model):
    '''
    所有model的一个积累，默认添加时间创建，时间更新
    '''
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(Base):
    __tablename__ = 'user'

    # 用数值表示角色，方便判断是否有权限，比如有个操作角色为员工
    # 以及以上的用户才可以做，那摩只要判断user.role >= ROLE_STAFF
    # 就可以了，数值之间设置了10的间隔时为了方便以后加入其他的角色
    ROLE_USER = 10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64),unique=True,nullable=False)
    # 默认情况下，sqlalchemy 会一字段名来定义列名，但这里是_password,所以明确指定数据库列名为password
    _password = db.Column('password',db.String(256),nullable=False)
    role = db.Column(db.SmallInteger,default=ROLE_USER)
    publish_courses = db.relationship('Course')

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        '''
        python风格的getter
        :return:
        '''
        return  self._password

    @password.setter
    def password(self,orig_password):
        '''
        python风格的setter,这样设置user.password就会自动为password生成哈希值存入_password
        :param orig_password:
        :return:
        '''
        self._password = generate_password_hash(orig_password)

    def check_password(self,password):
        '''
        判断用户输入的密码和存储的hash密码是否相等
        :param password:
        :return:
        '''
        return check_password_hash(self._password,password)

    @property
    def is_admin(self):
        return  self.role == self.ROLE_ADMIN
    @property
    def is_staff(self):
        return  self.role == self.ROLE_STAFF

class Course(Base):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    author= db.relationship('User', uselist=False)