from flask import  Flask ,render_template
from demo20.mongo import  waiwei_list ,get_detail

app = Flask(__name__)


@app.route('/')
def index():
    data,count = waiwei_list()
    # count = len(list(data))
    return  render_template('index.html',data = data ,count=count)


    return  render_template('index.html',data=today_data,count=count)
@app.route('/detail/<string:name>')
def detail(name):

    data = get_detail(name)
    return  render_template('detail.html',data=data)
#
# @app.route('/list')
# def list():
#
#     data,count = select_gupiao_list()
#     return  render_template('detail.html',data=data,count=count)
if __name__ == '__main__':
    app.run(debug=True)