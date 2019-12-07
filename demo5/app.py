#encoding:utf-8

from flask import  Flask ,render_template , request,url_for,flash,send_from_directory ,redirect
# from flask_wtf.csrf import  CSRFProtect
import  os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
from forms import BaseLogin ,UploadForm
import  time
import  os
import  platform
import  config


app = Flask(__name__)
app.config.from_object(config)
# if platform.system() == "Windows":
#     slash = '\\'
# else:
#     platform.system()=="Linux"
#     slash = '/'
slash = '/'
UPLOAD_PATH = os.path.curdir + slash + 'uploads' + slash

@app.route('/')
def hello_world():
    return  render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = BaseLogin()

    if form.validate_on_submit():
        flash(form.name.data+"|"+form.password.data)
        return '表单数据提交成功'
    else:
        return render_template('login.html', form=form)

@app.route('/upload',methods=['GET','POST'])
def upload():

    if request.method == 'GET':
        return  render_template('upload.html')
    else:
        if not os.path.exists(UPLOAD_PATH):
            os.makedirs(UPLOAD_PATH)  # 没有目录则创建目录
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        print(form.file.data)
        if form.validate():
            f = request.files['file']
            filename = secure_filename(f.filename)  # 取得文件名字
            ext = filename.rsplit('.', 1)[1]  # 获取文件后缀
            unix_time = int(time.time())
            new_filename = str(unix_time) + '.' + ext  # 对文件进行重新命名
            file_url = UPLOAD_PATH + new_filename
            print(new_filename)
            print(UPLOAD_PATH)
            print(file_url)
            f.save(os.path.join(UPLOAD_PATH, new_filename))
            flash("上传文件成功！！")
            return redirect(url_for('show_images'))

        else:
            return '只能上传图片文件'


def find_file(path):
    result = os.walk(path)
    print(result)
    for i in result:
        path1 = i[0]
        files = i[2]
        print(path1)
        print(files)
    return  files,path1

@app.route('/images')
def show_images():
    files,path1 = find_file(UPLOAD_PATH)
    return  render_template('image_list.html',files=files)


#访问上传的文件
#浏览器访问：http://127.0.0.1:5000/images/xxx.jpg/  就可以查看文件了
@app.route('/images/<filename>/',methods=['GET','POST'])
def get_image(filename):
    dirpath = os.path.join(app.root_path, 'uploads')#得到绝对路径，比如J:\python project\例5-3-2\uploads
    print(dirpath)
    print(filename)
    #return send_from_directory(dirpath,filename,as_attachment=True)#为下载方式
    return send_from_directory(dirpath,filename)#为在线浏览方式
if __name__ == '__main__':
    app.run(debug=True)

