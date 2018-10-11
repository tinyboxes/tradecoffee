# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TradecoffeeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    roaster = scrapy.Field()
    location = scrapy.Field()
    name = scrapy.Field()
    classification = scrapy.Field()
    roastlevel = scrapy.Field()
    descriptor = scrapy.Field()
    flavornotes = scrapy.Field()
    price = scrapy.Field()
    weight = scrapy.Field()
    country = scrapy.Field()
    country = scrapy.Field()
    region = scrapy.Field()
    subregion = scrapy.Field()
    elevation = scrapy.Field()
    process = scrapy.Field()
    varietal = scrapy.Field()
    method = scrapy.Field()
