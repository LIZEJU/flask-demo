from flask import Flask , render_template
from demo26.simpledu.config import  configs
from demo26.simpledu.modes import db , Course
from flask_migrate import Migrate

app = Flask(__name__)

def register_blueprints(app):
    from simpledu.handlers import front, course, admin , users
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(users)


def create_app(config):
    """ 可以根据传入的 config 名称，加载不同的配置
       """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # SQLAlchemy 的初始化方式改为使用 init_app
    db.init_app(app)
    Migrate(app,db)
    register_blueprints(app)
    # 路由函数暂时写在这里，后面会介绍使用 Flask 的 Blueprint 实现
    # 路由的模块化
    return app



app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True)