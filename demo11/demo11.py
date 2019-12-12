#encoding:utf-8

from flask import  make_response , Flask , render_template ,request
from datetime import  timedelta


app = Flask(__name__)
app.config.update({
    'SECRET_KEY':'123'
})

@app.route('/user/<username>')
def user_index(username):
    resp = make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    return  resp
@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello 123{}'.format(username)
if __name__ == '__main__':
    app.run(debug=True)

    '''
    runtimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
    app.config.update({
    'SECRET_KEY':'123'
    })
    '''