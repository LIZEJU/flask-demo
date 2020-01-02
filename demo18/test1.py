# 使用 csv 模块来保存文件
import csv
# 使用 asyncio 库来实现异步编程
import asyncio
# 使用 aiohttp 库来实现网络请求
import aiohttp
# 设置异步编程中的超时
import async_timeout
# 使用 scrapy 中的 HtmlResponse 构建并解析页面内容
from scrapy.http import HtmlResponse

# 输出的结果保存到 result 列表中，每个元素都是一个二元组（name, update_time）
results = []

# 定义获取网页内容的异步操作，注意定义的方式
async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

# 定义提取网页数据的函数
def parse(url, body):
    # 1. 构建 HtmlResponse 对象
    # 2. 使用 xpath 获取仓库的 name 和 update_time 数据
    # 3. 将提取的数据存入 results：results.append((name, update_time))
    response = HtmlResponse(url=url, body=body)
    for repository in response.css('li.public'):
        name = repository.xpath(
            './/a[@itemprop="name codeRepository"]/text()').re_first(r"\n\s*(.*)")
        update_time = repository.xpath(
            './/relative-time/@datetime').extract_first()
        results.append((name, update_time))



# 定义异步任务执行
async def task(url):
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession() as session:
        # 调用 fetch 获得 HTML 页面


        html = await fetch(session, url)
        parse(url, html.encode('utf-8'))
        # 调用 parse 解析页面并将获得的数据存入 results


# 主函数
def main():
    loop = asyncio.get_event_loop()
    url_list = ['https://github.com/shiyanlou?tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wNlQxNzozNjoxNSswODowMM4FkpW2&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yM1QxNDoxODoyMSswODowMM4By2VI&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0xOVQxMDoxMDoyMyswODowMM4BmcsV&tab=repositories'
    ]
    tasks = [task(url) for url in url_list]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('shiyanlou-repos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    main()