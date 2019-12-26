import  re
import  requests
import  json
from datetime import datetime ,timedelta

def get_data(pn):
    url = 'http://15.push2.eastmoney.com/api/qt/clist/get'

    data = {
        "cb": "jQuery11240966266733369791_1577110798126",
        "pn": pn,
        "pz": "20",
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "fid": "f26",
        "fs": "m:0 f:8,m:1 f:8",
        "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152",
        "_": "1577110798131",
    }
    headers = {
        "Referer": "http://quote.eastmoney.com/center/gridlist.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    }
    response = requests.get(url, headers=headers, params=data)

    yield response.text

def handler_data(data):
    pattern = re.compile('jQuery11240966266733369791_1577110798126\((.*?)\)')
    data = pattern.search(data)[1]
    print(data)
    data = json.loads(data)['data']['diff']
    print(data)
    print(type(data))
    return data

def select_now_data():
    from pymongo import MongoClient

    db = MongoClient(host='127.0.0.1', port=27017).gupiao
    # 查询最新的股票的数据：今天的：过滤筛选，分组：以日期分组
    # data = db.gupiao.find({'name':data['name']})
    # for i in data:
    #     print(i)

    big_day = datetime.now()+timedelta(days=1)
    log_day = datetime.now()

    pipeline = [
        {
            '$match':{
                '$and':[
                    {
                        'now_time': {'$lt': big_day.strftime('%Y-%m-%d')},
                    },
                    {
                        'now_time': {'$gt': log_day.strftime('%Y-%m-%d')},
                    }
                ]
            }
        },
    ]

    results = list(db.gupiao.aggregate(pipeline=pipeline))
    print(results)
    # print(datetime.now().strftime('%Y-%m-%d'))
    return results

def insert_now_data(datas):
    # 存储数据：mongo
    # 股票的名字为索引存储数据，以日期为顺序
    from pymongo import MongoClient

    db = MongoClient(host='127.0.0.1', port=27017).gupiao

    for data in datas:
        now_time = data['now_time']
        s = '15:00'
        now_time = re.search('.*?(\d+:\d+:\d+)', now_time)[1]
        if datetime.strptime(now_time,'%H:%M:%S') > datetime.strptime(s,'%H:%M'):
            print('股票交易下班了')
            continue
        item = db.gupiao.find_one({'name': data['name'], "now_time": data['now_time']})

        if item:
            print('mongo 没有插入数据')
            pass
        else:
            print('mongo插入数据')
            db.gupiao.insert_one(data)

def qingxi_data(data):
    gupiao_list = []
    for i in data:
        code = i.get('f12')  # 股票代码
        name = i.get('f14')  # 股票名称
        start_price = i.get('f17')  # 股票今天开始的价格
        now_price = i.get('f2')  # 股票现在的的价格
        now_high_price = i.get('f15')  # 股票现在最高的价格
        now_low_price = i.get('f16')  # 股票现在最低的价格
        before_price = i.get('f18')  # 股票昨天结束的价格
        # low_price = i.get('f16') # 股票今天最低的价格
        shangchi_date = i.get('f26')  # 股票上市的时间
        low_high_price = i.get('f4')  # 股票涨跌额
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 爬虫爬取的时间

        gupiao_list.append({'code': code, 'name': name, 'start_price': start_price, 'before_price': before_price,
                            'shangchi_date': shangchi_date, 'now_time': now_time,
                            'now_price': now_price, 'now_high_price': now_high_price, 'now_low_price': now_low_price,
                            'low_high_price': low_high_price})
    return  gupiao_list

if __name__ == '__main__':
    # pn = int(input('数据要爬取数据的页数'))
    # for pn in range(0,20):
    #     # print(pn+1)
    #     data = next(get_data(pn+1))
    #     handler_data(data)
        # print(next(data))
    data = next(get_data(1))
    data = handler_data(data)
    gupiao_list = qingxi_data(data)
    insert_now_data(gupiao_list)
    select_now_data()
