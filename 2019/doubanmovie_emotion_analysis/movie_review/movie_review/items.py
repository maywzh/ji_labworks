# -*- coding: utf-8 -*-


import scrapy


class MovieReviewItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_star = scrapy.Field()
    movie_quote = scrapy.Field()
    review = scrapy.Field()
    sentiment = scrapy.Field()
