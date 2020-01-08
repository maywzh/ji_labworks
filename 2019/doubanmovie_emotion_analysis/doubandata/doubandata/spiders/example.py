# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
