#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:34:52 2018

@author: dmorton
"""

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from uk2010.items import Uk2010Item


class Spider2010(CrawlSpider):
    name = "spider_2010"
    start_urls = ['http://news.bbc.co.uk/2/shared/election2010/results/']
    rules = (
        Rule(
            LxmlLinkExtractor(restrict_xpaths='.//div[@id="constituencycontainer"]//ol[@class="constituency-list"]//li',
                              unique=False),
            follow=True,
            callback='parse_constituency'),
    )

    def _get_result(self, constituency, candidate):
        result = Uk2010Item()
        result['constituency'] = constituency
        result['name'] = candidate[0].xpath('.//span/text()').extract()[0].strip()
        result['party'] = candidate[1].xpath('.//text()').extract()[0]
        result['votes'] = candidate[2].xpath('.//text()')[0].extract().replace(',', '')
        result['percent'] = candidate[3].xpath('.//text()')[0].extract().replace(',', '')
        result['percent_change'] = candidate[4].xpath('.//text()')[0].extract().replace(',', '').replace('+', '')
        return result

    def parse_constituency(self, response):
        page = Selector(response)
        page_table = page.xpath('.//table[@class="candidate-detail"]//tr[@class]')
        constituency = page.xpath('.//head/title/text()').extract()[0].split('|')[3].strip()
        candidates = [row.xpath('.//td') for row in page_table]

        return [self._get_result(constituency, c) for c in candidates]
