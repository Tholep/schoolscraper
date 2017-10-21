import sys
import os
# Add the ptdraft folder path to the sys.path list
sys.path.append(os.path.join(os.getcwd(), 'realestate'))
print sys.path
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy.loader import ItemLoader

from items import RealEstateInfo



import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import re
import pandas as pd

class myspider(scrapy.Spider):
    name = "realestate"
    allowed_domains=["muabannhadat.vn"]
    rules = (Rule(LinkExtractor(allow=()),callback='parse_item',follow=True))
    filter=r'http:\/\/www.muabannhadat.vn\/([\w\W]+)\/\w+'
    regex_schemes=re.compile(filter,re.IGNORECASE)
    
    def start_requests(self):
        #input real estate links

        urls=["http://www.muabannhadat.vn/can-ho-ban-chung-cu-3529/ban-nhanh-can-ho-thu-duc-chi-650tr-can-co-ban-cong-6224634","http://www.muabannhadat.vn/can-ho-ban-chung-cu-3529/ban-nhanh-can-ho-thu-duc-chi-650tr-can-co-ban-cong-6224634"]

        # send request to each links
        for url in urls:
            request=scrapy.Request(url=url, callback=self.parse_item)
            yield request

    def filter_links(self, links):
        print ('**************************************************************')
        for link in links:
            #if self.allowed_domains[0] not in link.url:
            print ('**************************************************************')
            print link.url

    def parse_item(self, response):

        loc=response.xpath('//span[@id="MainContent_ctlDetailBox_lblMapLink"]/a/@href').re(r'loc:(\d+\.\d+),(\d+\.\d+)')
        cost_extract=response.xpath('//span[@id="MainContent_ctlDetailBox_lblPrice"]/text()').extract()
        

        if loc and cost_extract:
            lon=str(loc[0])
            lat=str(loc[1])

            #cost_extract=response.xpath('//span[@id="MainContent_ctlDetailBox_lblPrice"]/text()').extract()
            cost_value=cost_extract[0].split()[0]
            if cost_value.isdigit():
                cost=str(cost_value) if float(cost_value) >50 else str(float(cost_value)*1000)
            else:
                cost="Secret"

            #extract street, award, district and city
            street=response.xpath('//span[@id="MainContent_ctlDetailBox_lblStreet"]/text()').extract()
            ward=response.xpath('//span[@id="MainContent_ctlDetailBox_lblWard"]/a/text()').extract()
            district=response.xpath('//span[@id="MainContent_ctlDetailBox_lblDistrict"]/a/text()').extract()
            city=response.xpath('//span[@id="MainContent_ctlDetailBox_lblCity"]/a/text()').extract()

            square_ext=response.xpath('//span[@id="MainContent_ctlDetailBox_lblSurface"]/text()').extract()
            square=str(square_ext[0].split()[0])

            category=self.regex_schemes.search(response.url).groups(1)[0]

            date_created=response.xpath('//span[@id="MainContent_ctlDetailBox_lblDateCreated"]/a/text()').extract()
            date_modified=response.xpath('//span[@id="MainContent_ctlDetailBox_lblDateUpdated"]/a/text()').extract()

            l = ItemLoader(item=RealEstateInfo(), response=response)
            l.add_value('lon',lon)
            l.add_value('lat',lat)
            l.add_value('cost',cost)
            l.add_value('square',square)
            l.add_value('category',category)
            if street:
                l.add_value('street',street[0].encode('utf-8'))
            if ward:
                l.add_value('ward',ward[0].encode('utf-8'))
            if district:
                l.add_value('district',district[0].encode('utf-8'))
            if city:
                l.add_value('city',city[0].encode('utf-8'))
            l.add_value('url',response.url)
            
            l.add_value('date_created',date_created)
            if date_modified:
                l.add_value('date_modified',date_modified)

            yield l.load_item()

        
        
        
        links = LinkExtractor().extract_links(response)
        if links is not None:
            for link in links:
                next_page = link.url
                
                yield scrapy.Request(next_page, callback=self.parse_item)

