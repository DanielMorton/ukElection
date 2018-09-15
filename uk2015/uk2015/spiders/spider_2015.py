#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 07:20:08 2018

@author: dmorton
"""

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from uk2015.uk2015.items import Uk2015Item


class Spider2015(CrawlSpider):
    name = "spider_2015"
    start_urls = ['https://www.bbc.co.uk/news/politics/constituencies']
    rules = (
        Rule(LxmlLinkExtractor(restrict_xpaths='.//table[@class="az-table"]',
                               unique=True),
             follow=True,
             callback='parse_constituency'),
    )

    def get_result_2015(self, label, constituency, candidate):
        result = Uk2015Item()
        result['year'] = 2015
        result['label'] = label
        result['constituency'] = constituency
        result['name'] = candidate.xpath('.//div[@class="party__name--candidate"]/text()').extract()[0].strip()
        result['party'] = candidate.xpath('.//div[@class="party__name--long"]/text()').extract()[0]
        result['votes'] = int(
            candidate.xpath('.//li[@class="party__result--votes essential"]/text()')[0].extract().replace(',', ''))
        result['percent'] = float(
            candidate.xpath('.//li[@class="party__result--votesshare essential"]/text()')[0].extract())
        result['percent_change'] = float(
            candidate.xpath('.//li[@class="party__result--votesnet essential"]/span/text()')[0].extract().replace('+',
                                                                                                                  ''))
        return result

    def get_result_2017(self, label, constituency, candidate):
        result = Uk2015Item()
        result['year'] = 2017
        result['label'] = label
        result['constituency'] = constituency
        result['name'] = candidate.xpath(
            './/td[@class="results-table__body-item results-table__body-item--constituency-candidates"]//span[@class="results-table__body-text"]//text()').extract()[
            0].strip()
        result['party'] = \
        candidate.xpath('.//p[@class="results-table__party-name-const-region--long"]/text()').extract()[0]
        result['votes'] = int(candidate.xpath(
            './/td[@class="results-table__body-item results-table__body-item--constituency"]//span//text()').extract()[
                                  1].replace(',', ''))
        result['percent'] = float(candidate.xpath(
            './/td[@class="results-table__body-item results-table__body-item--constituency"]//span//text()').extract()[
                                      3])
        result['percent_change'] = float(candidate.xpath(
            './/td[@class="results-table__body-item results-table__body-item--constituency"]//span//text()').extract()[
                                             5].replace('+', ''))
        return result

    def parse_constituency(self, response):
        page = Selector(response)
        label = response.url.split('/')[-1]
        constituency = page.xpath('.//h1[@class="constituency-title__title"]/text()').extract()[0]

        candidates2015 = page.xpath(
            './/div[@class="results-scoreboard election2015-results--constituency"]//div[@class="party"]')
        results2015 = [self.get_result_2015(label, constituency, c) for c in candidates2015]

        candidates2017 = page.xpath(
            './/table[@class="results-table results-table--constituency-region"]//tr[@class="results-table__body-row"]')
        results2017 = [self.get_result_2017(label, constituency, c) for c in candidates2017]

        return results2015 + results2017
