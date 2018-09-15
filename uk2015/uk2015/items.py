# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Uk2015Item(scrapy.Item):
    # define the fields for your item here like:
    year = scrapy.Field()
    label = scrapy.Field()
    constituency = scrapy.Field()
    party = scrapy.Field()
    name = scrapy.Field()
    votes = scrapy.Field()
    percent = scrapy.Field()
    percent_change = scrapy.Field()
