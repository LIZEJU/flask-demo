#encoding:utf-8

from flask import  Flask , url_for , redirect

app = Flask(__name__)

app.config.update({
    'SECRET_KEY':'A RANDOM STRING'
})

@app.route('/')
def index():
    return  'hello world!'

@app.route('/course/<name>')
def courses(name):
    return 'courses: {}'.format(name)

@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('courses',name='linux'))
    return  'test'

@app.route('/<username>')
def hello(username):
    if username == 'linux':
        return 'hello {}'.format(username)
    else:
        return  redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)