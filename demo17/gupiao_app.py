from flask import  Flask ,render_template
from get_gupiao import  select_gupiao_list,select_distinct_data,get_now_data , get_today_data

app = Flask(__name__)


@app.route('/')
def index():
    today_data = get_today_data()
    # data,count = select_distinct_data(today_data)
    count = len(today_data)

    return  render_template('index.html',data=today_data,count=count)
@app.route('/detail/<string:name>')
def detail(name):

    data = get_now_data(name)
    return  render_template('detail.html',data=data)

@app.route('/list')
def list():

    data,count = select_gupiao_list()
    return  render_template('detail.html',data=data,count=count)
if __name__ == '__main__':
    app.run(debug=True)