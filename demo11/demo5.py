#encoding:utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def user_index(username):
    return render_template('user_index.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)