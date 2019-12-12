#encoding:utf-8


from flask import  Flask , render_template  , abort
import  os
import  json

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

def file_split(filename):
    return  filename[:-5]
app.add_template_filter(file_split)
def file_list():
    result = os.walk(bashpath)
    file_list = []
    for i in result:
        file_list.extend(i[2])
    return  file_list
@app.route('/')
def index():
    # 显示文章名称的列表
    # 也就是 /home/shiyanlou/files/ 目录下所有 json 文件中的 `title` 信息列表
    file_lists = file_list()
    print(file_lists)
    return  render_template('index.html',file_lists=file_lists)


@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面
    filename_path = os.path.join(bashpath,filename)
    if not os.path.exists(filename_path):
        abort(404)
    with open(filename_path,'r',encoding='utf8') as f:
        data = json.load(f)
    return  render_template('file_detail.html',data=data)
@app.errorhandler(404)
def error_404(error):
    return  render_template('404.html'),404
if __name__ == '__main__':
    bashpath = os.path.join(os.path.dirname(__file__),'file')
    print(bashpath)
    app.run(debug=True)