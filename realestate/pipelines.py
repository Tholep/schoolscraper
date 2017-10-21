# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters  import CsvItemExporter
import datetime
import os
class RealestatePipeline(object):
	def __init__(self):
		if not os.path.exists(os.path.join(os.getcwd(), 'result')):
			os.mkdir("result")
		self.file = open("result/"+str(datetime.datetime.now())+".csv", 'wb')
		self.exporter = CsvItemExporter(self.file, unicode,fields_to_export=["lon","lat","square","cost","category","street","ward","district","city","date_created","date_modified","url"])
		self.exporter.start_exporting()
	def close_spider(self, spider):
		self.exporter.finish_exporting()
		self.file.close()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
