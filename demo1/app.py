#encoding:utf-8

from flask import  Flask , url_for , redirect , render_template

app = Flask(__name__)

@app.route('/')
def index():

    # url1 = url_for('user_login')
    # return redirect(url1)
    return  render_template('index.html')

@app.route('/user_login')
def user_login():
    return '这是用户登录页面,请您登录，才能访问首页' \
           ''
@app.route('/user/<string:name>')
def user(name):
    return  render_template('user.html',name=name)


if __name__ == '__main__':
    app.run(debug=True)