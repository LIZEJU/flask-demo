import  pymongo
from datetime import  datetime ,timedelta
from pymongo import MongoClient

db = MongoClient(host='127.0.0.1', port=27017).gupiao
def select_gupiao_list():
    data = db.gupiao.find({}).sort("now_time",-1)
    count = db.gupiao.count()

    return data , count
# 去重
def select_distinct_data():

    data = db.gupiao.distinct('name')
    count = len(data)
    return  data , count
def get_now_data(name):

    from pymongo import MongoClient

    db = MongoClient(host='127.0.0.1', port=27017).gupiao
    # 查询最新的股票的数据：今天的：过滤筛选，分组：以日期分组
    # data = db.gupiao.find({'name':data['name']})
    # for i in data:
    #     print(i)

    big_day = datetime.now() + timedelta(days=1)
    log_day = datetime.now()

    pipeline = [
        {
            '$match': {
                '$and': [
                    {
                        'now_time': {'$lt': big_day.strftime('%Y-%m-%d')},
                    },
                    {
                        'now_time': {'$gt': log_day.strftime('%Y-%m-%d')},
                    },
                    {
                        'name': name,
                    },
                ]
            },

        },
    ]

    results = list(db.gupiao.aggregate(pipeline=pipeline))
    print(results)
    # print(datetime.now().strftime('%Y-%m-%d'))
    return results
if __name__ == '__main__':
    # select_distinct_data()
    get_now_data('N华特')