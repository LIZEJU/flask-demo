# 使用 csv 模块来保存文件
import csv
# 使用 asyncio 库来实现异步编程
import asyncio
# 使用 aiohttp 库来实现网络请求
import aiohttp
# 设置异步编程中的超时
import async_timeout
import  re ,json
from datetime import  datetime
# 使用 scrapy 中的 HtmlResponse 构建并解析页面内容
from scrapy.http import HtmlResponse


# 输出的结果保存到 result 列表中，每个元素都是一个二元组（name, update_time）
results = []

# 定义获取网页内容的异步操作，注意定义的方式
async def fetch(session, url,pn):
    with async_timeout.timeout(10):
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
        async with session.get(url,headers=headers,params=data) as response:
            return await response.text()

# 定义提取网页数据的函数
def parse(url, data):
    pattern = re.compile('jQuery11240966266733369791_1577110798126\((.*?)\)')
    data = pattern.search(data)[1]
    print(data)
    data = json.loads(data)['data']['diff']
    for i in data:
        code = i.get('f12')  # 股票代码
        name = i.get('f14')  # 股票名称
        start_price = i.get('f17')  # 股票今天开始的价格
        now_price = i.get('f2')  # 股票现在的的价格
        now_high_price = i.get('f15')  # 股票现在最高的价格
        now_low_price = i.get('f16')  # 股票现在最低的价格
        before_price = i.get('f18')  # 股票昨天结束的价格
        shangchi_date = i.get('f26')  # 股票上市的时间
        low_high_price = i.get('f4')  # 股票涨跌额
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 爬虫爬取的时间
        results.append((code,name,start_price,now_price,now_high_price,now_low_price,before_price,shangchi_date,low_high_price,now_time))

# 定义异步任务执行
async def task(url):
    timeout = aiohttp.ClientTimeout(total=10)
    for i in range(1,20):
        async with aiohttp.ClientSession(timeout=timeout) as session:
            # 调用 fetch 获得 HTML 页
            html = await fetch(session, url,i)
            parse(url, html)
            # 调用 parse 解析页面并将获得的数据存入 results


# 主函数
def main():
    # 回调
    loop = asyncio.get_event_loop()
    url = 'http://15.push2.eastmoney.com/api/qt/clist/get'

    # 任务
    tasks = [task(url) ]
    loop.run_until_complete(asyncio.gather(*tasks))
    now_datatime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    print('现在的时间',now_datatime)
    f =  open('%s_gupiao.csv'%now_datatime, 'w', encoding='utf8',newline='')
    writer = csv.writer(f)
    writer.writerows(results)
    f.close()
if __name__ == '__main__':
    import  time

    while True:
        main()
        time.sleep(3600)