# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy_selenium import SeleniumRequest
from tradecoffee.items import TradecoffeeItem
import re


class TradeSpider(Spider):
    name = 'trade'
    allowed_urls = ['https://www.drinktrade.com/']
    start_urls = ['https://www.drinktrade.com/coffee/all-coffee/']

    def parse(self, response):
        # Find the total number of entries on the page so that we can decide how many urls to scrape next

        n_coffee = response.xpath('//span[@class="filter-qty text-body-2-desktop"]/text()').extract_first().split(' ')[0]
        n_coffee = int(n_coffee)

        # Find url to coffee detail
        detail_xpath = ['//div[@data-reactid="318"]/div[{}]/div/a/@href'.format(x) for x in range(1, 24)]

        #detail_xpath = ['//div[@data-reactid="318"]/div[{}]/div/a/@href'.format(x) for x in range(1, 22)]

        # List comprehension to construct all the detail urls
        urls = [response.xpath(path).extract_first() for path in detail_xpath]
        #only gets first 20 urls
        detail_urls = ['https://www.drinktrade.com{}'.format(url) for url in urls]

        print(n_coffee)
        print('-' * 25)
        print(detail_xpath)
        print(detail_urls)


        # Yield the requests to different search result urls,
        # using parse_result_page function to parse the response.
        for url in detail_urls:
            yield Request(url, callback=self.parse_detail_page)

        # This fucntion parses the product detail page.
    def parse_detail_page(self, response):

        # Extract each field from the page

        name = response.xpath('//h1[@class="product-name text-display-2-mobile text-display-2-desktop"]/text()').extract_first()
        roaster = response.xpath('//h2[@class="roaster-name text-title-mobile text-title-desktop"]/text()').extract_first()
        descriptor = response.xpath('//div[@class="description-container text-body-2-mobile text-body-2-desktop"]/text()').extract_first()
        flavornotes = response.xpath('//ul[@class="taste-features"]/li/text()').extract_first()
        price = response.xpath('//span[@class="product-price"]/text()').extract_first()
        weight = response.xpath('//span[@class="product-size"]/text()').extract_first()

        #print(name)
        #print(roaster)
        #print(descriptor)
        #print(flavornotes)
        #print(price)
        #print(weight)
        print('*' * 50)

        item = TradecoffeeItem()

        item['name'] = name
        item['roaster'] = roaster
        item['descriptor'] = descriptor
        item['flavornotes'] = flavornotes
        item['price'] = price
        item['weight'] = weight

        yield item
