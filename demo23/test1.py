# 需要使用 JSON 包解析 JSON 文件
import json
import pandas as pd
import  os

def analysis(file, user_id):
    times = 0
    minutes = 0
    with open(file,'r',encoding='utf8') as f:
        data = json.load(f)
    print(data[1])
    # print(type(data[1]))
    # print(data[1].keys())
    index = list(data[1].keys())
    print(index)
    '''
    补充代码：
    1. 使用 Pandas 读取数据
    2. 使用 Pandas 选择数据
    '''
    result = [[ i[j] for i in data for j in index]]
    df1 = pd.Series(result,index=index)
    print(df1)
    return times, minutes

if __name__ == '__main__':
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'user_study.json')
    print(path)
    user_id = '199071'
    analysis(path,user_id)