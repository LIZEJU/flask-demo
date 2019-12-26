import sys
from pymongo import MongoClient

mongo = MongoClient(host='127.0.0.1',port=27017).shiyanlou

def get_rank(user_id):
    client = MongoClient(host='127.0.0.1',port=27017)
    db = client.shiyanlou

    # 统计用户的总分数和总提交时间
    pieline = [
        # 选取指定用户的记录
        {'$match':{'user_id':user_id}},
        {'$group':{
            '_id':'$user_id',
            'total_score':{'$sum':'$score'},
            'total_time':{'$sum':'$submit_time'}
        }}
    ]

    results = list(db.contests.aggregate(pipeline=pieline))
    # print(results)
    if len(results) == 0 :
        return 0,0,0
    data = results[0]
    print('data:',data)
    # 计算指定用于的排名信息
    pipeline = [
        # 分组计算所有用户的总分数和总时间
        {'$group':{
            '_id':'$user_id',
            'total_score':{'$sum':'$score'},
            'total_time':{'$sum':'$submit_time'}
        }},
        # 从上一步的分组结果集里筛选出指定用户高或者总分相等但总时间较少的
        {'$match':{
            '$or':[
                {'total_score':{'$gt':data['total_score']}},
                {'total_time':{'$lt':data['total_time']},
                'total_score':data['total_score']
                 },
            ]
        }},
        {'$group':{'_id':None,'count':{'$sum':1}}}
    ]

    results = list(db.contests.aggregate(pipeline=pipeline))
    if len(results) > 0 :
        rank = results[0]['count'] + 1
    else:
        rank = 1
    return  rank , data['total_score'] , data['total_time']
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
    print(userdata)