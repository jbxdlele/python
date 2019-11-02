# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JobspiderItem(scrapy.Item):
    name = scrapy.Field()
    city = scrapy.Field()
    pub_date = scrapy.Field()
    salary = scrapy.Field()


class JobrequireItem(scrapy.Item):
    name = scrapy.Field()
    city = scrapy.Field()
    pub_date = scrapy.Field()
    salary = scrapy.Field()
    require = scrapy.Field()
