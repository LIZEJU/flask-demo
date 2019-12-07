#encoding:utf-8

from flask import  Flask, Response
from blue_admin import bp

app = Flask(__name__)
app.register_blueprint(bp)

app.config['SERVER_NAME'] = 'baidu.com:5000'

@app.route('/')
def set_cookie():

    resp = Response('设置cookie')

    resp.set_cookie('username','zhangsan',domain=".baidu.com")
    return resp

if __name__ == '__main__':
    app.run(debug=True)