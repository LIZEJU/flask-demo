import requests
import  re
# 使用 csv 模块来保存文件
import csv
from datetime import datetime
import sys
from scrapy.http import HtmlResponse
import  pymongo
def get(url):
    headers = {
        "Host": "toseseni.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Accept": "text/css,*/*;q=0.1",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.2.1091811495.1577364263; _gid=GA1.2.217545815.1577624026; _gat_gtag_UA_154970225_1=1",
    }
    response = requests.get(url,headers=headers)

    return  response.url,response.text,response.status_code
def parse(url,body):
    html = HtmlResponse(url=url,body=body.encode('utf8'))

    for x in html.xpath('//div[@class="post-list"]/article'):
        title = x.xpath('.//h2[@itemprop="name headline"]/text()').extract_first()
        img_url = x.xpath('.//a[@class="thumb"]/@style').extract_first()
        pattern = re.compile('background-image: url\(\'(.*?)\'')
        img_url = pattern.search(img_url)[1]
        print(title,img_url)
        # results.append((title,img_url))
        results.append({'title':title,'img_url':img_url})
def write_csv():
    now_datatime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    f = open('%s_meinv.csv' % now_datatime, 'w', encoding='utf8', newline='')
    writer = csv.writer(f)
    writer.writerows(results)
    f.close()

def write_mongo(data):
    mo = pymongo.MongoClient(host='127.0.0.1',port=27017).waiwei

    if mo.meinv.find_one({'title':data['title']}):
        mo.meinv.update_one({'title':data['title']},{ "$set":data})
    else:
        mo.meinv.insert_one(data)

def get_url(pn):
    url = 'https://toseseni.com/category/%E5%85%BC%E8%81%8C/page/{}/'.format(pn)
    print(url)
    return  url

if __name__ == '__main__':
    results = []
    count = 0
    import  time ,random
    for i in range(1, 100):
        try:
            url = get_url(i)
            url, body,code = get(url)
            parse(url, body)

            sleep_time = random.randint(1,9)
            print('休息时间：%s'%sleep_time)
            time.sleep(sleep_time)
            if str(code) == '404':
                break
        except Exception as e:
            count +=1
            if count >5:
                break
    # write_csv()
    for i in results:
        write_mongo(i)

