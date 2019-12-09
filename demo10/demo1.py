#encoding:utf-8

'''
爬取飞卢小说：一章小说的内容
https://b.faloo.com/p/639238/3.html


'''
import  requests
from requests.packages import urllib3
from scrapy.http import HtmlResponse

urllib3.disable_warnings()
url1 = 'https://b.faloo.com/p/639238/3.html'
url2 = 'https://b.faloo.com/f/639238.html'
def get_page(url):


    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "host4chongzhi=https%3a%2f%2fwww.baidu.com%2flink%3furl%3dVlLeOVlW4Ny9R8-WxRfcW9k4Ssak5hBvMcY7wcs3gs3; Hm_lvt_6d308f6626f6d0864b6bb4f348f2b5e5=1575819981; nc_rela=1; novelrelative=639238; curr_url=https%3A//b.faloo.com/p/639238/3.html; favorates28=639238%2C4; autobuychapters28=639238%2C4; Hm_lpvt_6d308f6626f6d0864b6bb4f348f2b5e5=1575820398",
        "Host": "b.faloo.com",
        "Referer": "https://b.faloo.com/p/639238/2.html",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    }

    response = requests.get(url,headers=headers,verify=False)
    with open('test.html','w',encoding='utf8') as f:
        f.write(response.text)
    return  response

def parse_body(response):
    html_text = HtmlResponse(url=response.url,body=response.content)
    body = html_text.xpath('//div[@class="main0"]/div[@id="content"]//text()').extract()
    title = html_text.xpath('//div[@class="main0"]/div[@id="title"]/h1/text()').extract_first().strip().strip('\r\n')
    content = ''
    for i in body:
        content += i
    with open("{}.txt".format(title),'w') as f:
        f.write(title)
        f.write(content)

def get_xiaoshuo_url():
    response = get_page(url2)
    html_text = HtmlResponse(url=response.url, body=response.content)
    first_xpath = html_text.xpath('//div[@class="ni_list"]/table')
    url_list1 = []
    for i in first_xpath:
        url_list = i.xpath('.//td[@class="td_0"]/a/@href').extract()
        url_list1.extend(url_list)
    # for i in url_list1:
    #     print(i)
    return  url_list1
if __name__ == '__main__':

    url_list1= get_xiaoshuo_url()
    count = 0
    while True:
        try:
            url = url_list1[count]
            print(url)
            import  urllib.parse
            url = urllib.parse.urljoin('https:',url)
            print(url)
            html_text = get_page(url)
            count += 1
            parse_body(html_text)
            import  time
            time.sleep(1.5)
        except Exception as e:
            print(e)
            break
