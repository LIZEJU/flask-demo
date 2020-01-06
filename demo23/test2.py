# 需要使用 JSON 包解析 JSON 文件
import json
import pandas as pd
import  os

def analysis(file, user_id):
    times = 0
    minutes = 0
    data = pd.read_json(file)
    # print(data)
    data_1 = data[data['user_id'] == user_id ]

    # print('查找的个人的数据：',data_1)
    times = len(data_1) # 个人学习的次数
    minutes = data_1['minutes'].sum()
    # count = 0
    # for i in data_1['minutes']:
    #     count += i
    # print(count)
    # print(minutes)
    return times, minutes
def analysis_raw(file, user_id):
    """从 file json 文件中统计出 user_id 指定用户的学习数据, 纯 python 实现

    Args:
        file(str): json file name
        user_id(int): user id
    """

    times = 0
    minutes = 0

    try:
        f = open(file)
        records = json.load(f)
        for item in records:
            if item['user_id'] != user_id:
                continue
            times += 1
            minutes += item['minutes']
        f.close()
    except:
        pass
    return times, minutes

if __name__ == '__main__':
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'user_study.json')
    # print(path)
    user_id =  199071
    times , minutes = analysis(path,user_id)
    print('{} 学习的时间次数：{}，学习的总时间：{}'.format(user_id,times,minutes))