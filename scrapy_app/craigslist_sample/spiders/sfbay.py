# -*- coding: utf-8 -*-
import scrapy
from craigslist_sample.items import CraigslistSampleItem


class SfbaySpider(scrapy.Spider):
    name = 'sfbay'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://ames.craigslist.org/search/cta?query=Ford&min_price=2000&max_price=5000']

    def parse(self, response):
        items = []
        hxs = scrapy.selector.HtmlXPathSelector(response)
        titles = hxs.select("//p[@class='result-info']")

        for t in titles:
            item = CraigslistSampleItem()
            item["title"] = t.select("a/text()").extract()
            item["link"] = t.select("a/@href").extract()
            items.append(item)
        return items

