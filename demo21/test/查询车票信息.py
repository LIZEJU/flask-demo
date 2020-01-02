from demo21.config.emailConf import sendEmail
import requests
import  os
def station_table( from_station, to_station):
    """
    查询车层的信息
    :param station:
    :return:
    """
    # 查询接口
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
    # 参数： get方法
    params = {
        "leftTicketDTO.train_date": date_time,
        "leftTicketDTO.from_station": get_city_code(from_station,to_station)[0],
        "leftTicketDTO.to_station": get_city_code(from_station,to_station)[1],
        "purpose_codes": "ADULT",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=3BCEF5F9D2A06DBC050EAEFE42D36D01; _jc_save_wfdc_flag=dc; RAIL_EXPIRATION=1577908951134; RAIL_DEVICEID=WBgNfcEO-rxXxVggQy1-AtuymWFwmc9Ix0i_8V9yfT7Q2RpdDH3a_CJhq8GZr-daRAi7jZC2ei54klxe2QvBPR0cD1VXfrWOxLFC0e4TObzhG1jSdWg424FsHVJ64Uyxn5nX0y4a4rAeK5DUYHtxpfOkhM0qjPSo; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1356398858.24610.0000; _jc_save_fromStation=%u6DF1%u5733%2CSZQ; _jc_save_toStation=%u676D%u5DDE%2CHZH; _jc_save_toDate=2019-12-31; _jc_save_fromDate=2020-01-02",
        "Host": "kyfw.12306.cn",
        "If-Modified-Since": "0",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%B7%B1%E5%9C%B3,SZQ&ts=%E6%9D%AD%E5%B7%9E,HZH&date=2019-12-31&flag=N,N,Y",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",

    }
    response = requests.get(url, headers=headers, params=params)
    print(response.url)
    # text = response.text
    import json
    text_1 = json.loads(response.text)
    str_1 = ''.join(text_1['data']['result'])
    list_1 = text_1['data']['result']
    # path = os.path.join(os.path.dirname(__file__), '../station_name.txt')
    # for i in list_1:
    #     print(i)
    #     with open(path,'a',encoding='utf8')as f:
    #
    #         f.write('@'+i+'\n')

    # with open(path,'r',encoding='utf8') as f:
    #     info = f.read().split('@')
    # print(info)
    # count = 0
    result = []
    for i in  list_1:
        # print(i.strip())
        # count += 1
        # print(count)
        result.append(i.strip().split('|'))
    # print(result)
    r_data = []
    result1 = []
    for i in result:
        if i is None or i == ['']:
            result.remove(i)
            continue
        # print(i)
        # if 'D2294' in i :
        #     code = i.index('D2294')
        #     print(code)
        # print(i[3])  # 车次
        # print(i[6])  # 车起始位置标签
        # print(i[7])  # 车终点位置标签
        # print(i[8])  # 车起始时间
        # print(i[9])  # 车终点时间
        # print(i[10])  # 车旅途花费的时间
        # count = 0
        # print('打印每个车次的信息')
        # for d in i:
        #
        #     print(str(d)+'==='+str(count))
        #     count += 1
        # print(i[3]) # 车次
        # print(i[26]) # 是否有座 --- 无座位
        # print(i[30]) # 是否有座----二等座
        # print(i[31]) # 是否有座---一等座
        code = i[3]
        er_deng = i[30]
        start = i[6]
        end = i[7]
        start_time = i[8]
        end_time = i[9]
        total_time = i[10]

        if i[30] == '有' or type(er_deng) == 'int':
            print('发送邮件')
            msg1 = 'code:{},tickent_num:{}：start：{}，end：{}：start_time：{},end_time:{},total_time:{}'.format(code,
                                                                                                           er_deng,
                                                                                                           get_code_city(
                                                                                                               start),
                                                                                                           get_code_city(
                                                                                                               end),
                                                                                                           start_time,
                                                                                                           end_time,
                                                                                                           total_time)
            # print(msg1)
            msg = '<p>{}</p>'.format(msg1)
            # sendEmail(msg1)
            result1.append(msg)
    if result1 != []:
        print(result1)
        sendEmail(''.join(result1),'3265218750@qq.com')

def get_city_code(from_station,to_station):
    import pymongo
    mo = pymongo.MongoClient().city
    code1 = mo.citymap.find_one({'name':from_station},{'_id':0,'code':1})
    code2 = mo.citymap.find_one({'name':to_station},{'_id':0,'code':1})

    result = [code1['code'],code2['code']]
    print(result)
    return result

def get_code_city(code):
    import pymongo
    mo = pymongo.MongoClient().city
    name = mo.citymap.find_one({'code': code}, {'_id': 0, 'name': 1})
    return name['name']
if __name__ == '__main__':
    import  random
    # from_station = input('请输入起始地址')
    # to_station = input('请输入终点地址')
    # date_time = input('请输入要查询火车票的日期：yyyyxxzz')
    # receiver = input('请输入接受邮件的邮箱：》》')
    list_city = ['北京','杭州','齐齐哈尔','上海','衡水']
    from_station = random.choice(list_city)
    to_station = '沈阳'
    date_time = '2020-01-20'
    station_table(from_station,to_station)
