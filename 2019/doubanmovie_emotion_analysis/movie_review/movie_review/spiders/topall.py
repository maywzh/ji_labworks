# -*- coding: utf-8 -*-
import re
import csv

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector


class DouBanSpider(scrapy.Spider):
    name = 'topall'

    def start_requests(self):
        for i in range(0, 250, 25):
            url = 'https://movie.douban.com/top250?start={}&filter='.format(
                str(i))
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for movie in movies:
            movie_url = "".join(movie.xpath(
                'div[@class="hd"]/a/@href').extract())
            yield Request(url=movie_url, callback=self.parse)
            movie_name = movie.xpath(
                'div[@class="hd"]/a/span/text()').extract()
            movie_name_join = "".join(movie_name) .replace('\t', '').replace(
                '\n', '').replace('\xa0', '').replace('\ufeff', '').replace('\u200b', '')
            movie_star = movie.xpath(
                'div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            movie_star_int = "".join(movie_star)
            movie_quote = movie.xpath(
                'div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
            movie_quote_join = "".join(movie_quote) .replace('\t', '').replace(
                '\n', '').replace('\xa0', '').replace('\ufeff', '').replace('\u200b', '')
            # if movie:
            #     with open('./data/movie.csv', 'a+') as f:
            #         csv_write = csv.writer(f)
            #         data_row = [movie_url, movie_name_join,
            #                     movie_star_int, movie_quote_join]
            #         csv_write.writerow(data_row)

            print(movie_url)

        def get_movie_info(self, response):
            selector = Selector(response)
            print("GET " + response.xpath(
                'div[@id="info"]/span/span[@class="pl"]').extract())
