# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
    # 阅读数量
    number = scrapy.Field()

# item {"title":"","time":"","number":""}





