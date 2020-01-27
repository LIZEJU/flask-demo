# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/26 9:56 PM
# Project: flask-demo

import scrapy

class CoursesSpider(scrapy.Spider):

    name = 'courses'

    start_urls = ['https://www.shiyanlou.com/bootcamp/']

    def parse(self, response):
        for course in response.css('div.row div.col-3'):
            yield {
                'name': course.xpath('.//div[@class="course-body"]/p[1]/text()').extract_first().strip(),
                'description': course.xpath('.//div[@class="course-body"]/p[2]/text()').extract_first().strip(),
                'image_url': course.xpath('.//div[@class="course-header relative"]/img/@src').extract_first()
            }

