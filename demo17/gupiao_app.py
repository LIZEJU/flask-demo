from flask import  Flask ,render_template
from get_gupiao import  select_gupiao_list,select_distinct_data,get_now_data

app = Flask(__name__)


@app.route('/')
def index():

    data = select_distinct_data()
    return  render_template('index.html',data=data)
@app.route('/detail/<string:name>')
def detail(name):

    data = get_now_data(name)
    return  render_template('detail.html',data=data)
if __name__ == '__main__':
    app.run(debug=True)