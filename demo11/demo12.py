#encoding:utf-8

from flask import  make_response , Flask , render_template ,request
from datetime import  timedelta


app = Flask(__name__)
app.config.update({
    'SECRET_KEY':'123'
})


@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']

        import  random
        resp = make_response(render_template('cookie_index.html'))
        resp.set_cookie('username',user)
        # resp.set_cookie('useid',random.randint(1,100))
        return  resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('username')
    return '<h1>welcome, '+name+'</h1>'
if __name__ == '__main__':
    app.run(debug=True)

    '''
    runtimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
    app.config.update({
    'SECRET_KEY':'123'
    })
    '''