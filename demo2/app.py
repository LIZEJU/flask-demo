#encoding:utf-8

from flask import  Flask ,render_template


app = Flask(__name__)


@app.route('/')
def index():
    goods = [
        {
            'name': 'apple'
        },
        {
            'name':'steam'
        },
        {
            'name': 'pear'
        },
        {
            'name': 'bana'
        },
        {
            'name': 'tear'
        },
        {
            'name': 'water'
        },
    ]
    return  render_template('goods.html',**locals())

def do_index_class(index):
    if index % 3 == 0 :
        return  'line'
    else:
        return  ''

app.add_template_filter(do_index_class,'index_class')

def my_test():
    return  '这是测试页面'

app.add_url_rule('/test',endpoint='tests',view_func=my_test)

if __name__ == '__main__':
    app.run(debug=True)