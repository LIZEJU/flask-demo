#encoding:utf-8

from flask import  session , Flask
from datetime import  timedelta


app = Flask(__name__)
app.config.update({
    'SECRET_KEY':'123'
})

@app.route('/set_session')
def set_session():
    session.permanent = True

    app.permanent_session_lifetime = timedelta(minutes=1)

    session['username'] = 'shiyanlou'

    return '成功设置session'

@app.route('/get_session')
def get_session():
    value = session.get('username')
    return '获取session的值为：{}'.format(value)

if __name__ == '__main__':
    app.run(debug=True)

    '''
    runtimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
    app.config.update({
    'SECRET_KEY':'123'
    })
    '''