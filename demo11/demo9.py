#encoding:utf-8

from flask import  Flask , url_for , redirect ,request

app = Flask(__name__)

@app.route('/httptest',methods=['GET','POST'])
def httptest():
    if request.method == 'GET':
        t = request.args.get('t',default='t')
        q = request.args.get('q',default='q')

        return "{}:{}".format(t,q)
    else:
        q = request.form.getlist('Q')
        print(q)
        return "{}".format(q)

if __name__ == '__main__':
    app.run(debug=True)