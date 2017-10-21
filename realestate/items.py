# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RealEstateInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #address=scrapy.Field()
    lon=scrapy.Field()
    lat=scrapy.Field()
    square=scrapy.Field()
    cost=scrapy.Field()
    category=scrapy.Field()
    street=scrapy.Field()
    ward=scrapy.Field()
    district=scrapy.Field()
    city=scrapy.Field()
    url=scrapy.Field()
    date_created=scrapy.Field()
    date_modified=scrapy.Field()
