#encoding:utf-8

from flask import  Flask

app = Flask(__name__)

app.config.update({
    'SECRET_KEY':'A RANDOM STRING'
})

@app.route('/')
def index():
    return  'hello world!'

@app.route('/user/<username>')
def user_index(username):
    return 'hello {}'.format(username)
if __name__ == '__main__':
    app.run(debug=True)