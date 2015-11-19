# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title=scrapy.Field()#电影名
    rank=scrapy.Field()#上映年份
    score=scrapy.Field()#豆瓣分数
    director=scrapy.Field()#导演
    classification=scrapy.Field()#分类
