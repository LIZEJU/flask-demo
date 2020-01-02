import  requests


def get_method(url):
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

    response = requests.get(url,headers=headers)

    return  response.text

if __name__ == '__main__':
    url = 'https://www.12306.cn/index/script/core/common/station_name_v10071.js'
    # city_str = get_method(url)
    with open('city.txt','r',encoding='utf8') as f:
        import re
        data = f.read()
        print(data)
        d_1 = data.split('=')
        print(d_1[1])
        j_1 = d_1[1].split('@')
        print(j_1[-1].strip(';').strip('\''))
        print('循环遍历',len(j_1))
        result = []
        for i in j_1:
            data = i.strip(';').strip('\'')
            if data == '':
                j_1.remove(i)
            else:
                print(data)
                result.append(data.split('|'))
        print(len(j_1))
        print(result)

        city_dict = {}
        for i in result:
            city_dict[i[1]] = i[2]
        import  pymongo
        mo = pymongo.MongoClient().city


        for i in city_dict:
            # print(i,city_dict[i])
            if mo.citymap.find_one({'name':i}):
                pass
            else:
                mo.citymap.insert_one({'name':i,'code':city_dict[i]})
        data = mo.citymap.find({},{'name':1,'code':1})
        for i in data:
            print(i)
        print('mongo查询')
        print(mo.citymap.find().count())
        print('mongo查询深圳')
        print(mo.citymap.find_one({'name':'深圳'},{'_id':0,'code':1}))
        print(mo.citymap.find_one({'name':'杭州'},{'_id':0,'code':1}))
        print(mo.citymap.find_one({'name':'朔州'},{'_id':0,'code':1}))

