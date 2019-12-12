一个简单的问答网站：
wget http://labfile.oss.aliyuncs.com/courses/923/week2/helloshiyanlou.json

wget http://labfile.oss.aliyuncs.com/courses/923/week2/helloworld.json

result = os.walk()
result[2] 文件列表
result[1] 文件路径


json
json.load(f) 加载文件中的json字符串---json数据

404 页面的设置
app.errorhandler(404)
def error_404(error):
    return render_template('index.html'),404


os.exist()判断文件是否存在

abort(404) 走404错误的页面

添加自定义过滤器
def file_split(filename):
    return  filename[:-5]
app.add_template_filter(file_split)



