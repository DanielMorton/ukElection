# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Uk2010Item(scrapy.Item):
    # define the fields for your item here like:
    label = scrapy.Field()
    constituency = scrapy.Field()
    party = scrapy.Field()
    name = scrapy.Field()
    votes = scrapy.Field()
    percent = scrapy.Field()
    percent_change = scrapy.Field()
