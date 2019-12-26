import sys
from pymongo import MongoClient

mongo = MongoClient(host='127.0.0.1',port=27017).shiyanlou

def get_rank(user_id):
    client = MongoClient(host='127.0.0.1',port=27017)
    db = client.shiyanlou

    data = db.contests.find_one({"user_id":user_id})
    print(data)
if __name__ == '__main__':

    '''
    1. 判断参数格式是否符合要求
    2. 获取 user_id 参数
    '''
    if len(sys.argv) != 2:
        print('parameter error')
        sys.exit(1)

    user_id = int(sys.argv[1])
    # 根据用户 ID 获取用户排名，分数和时间
    userdata = get_rank(user_id)
    # print(userdata)