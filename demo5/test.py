#encoding:utf-8
import  os

slash = '/'
UPLOAD_PATH = os.path.curdir + slash + 'uploads' + slash

bashpath = os.path.join(os.path.dirname(__file__),'uploads')

def find_file(path):
    result = os.walk(path)
    print(result)
    for i in result:
        path1 = i[0]
        files = i[2]
        print(path1)
        print(files)
    return  files,path1

print(bashpath)
find_file(UPLOAD_PATH)