# -*- coding: utf-8 -*-

# Scrapy settings for tradecoffee project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from shutil import which

BOT_NAME = 'tradecoffee'

SPIDER_MODULES = ['tradecoffee.spiders']
NEWSPIDER_MODULE = 'tradecoffee.spiders'


SELENIUM_DRIVER_NAME='chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH=which('Webdriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tradecoffee (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tradecoffee.pipelines.WriteItemPipeline': 300,
}
