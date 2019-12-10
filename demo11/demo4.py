#encoding:utf-8

from flask import  Flask , url_for , redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello pwd'

@app.route('/courses/<name>')
def courses(name):
    if name == 'java':
        return  redirect(url_for('index'))
    else:
        return  'linux'

@app.route('/test')
def test():
    print('http://127.0.0.1:5000/courses/java')
    print(url_for('courses',name='java'))
    import  time
    time.sleep(10)
    return  redirect(url_for('courses',name='java'))

if __name__ == '__main__':
    app.run(debug=True)