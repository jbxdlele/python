# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class JobspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

import csv
import codecs
from .items import *


class JobspiderPipeline_one(object):
    def __init__(self):
        self.file = codecs.open('51job.csv', 'w', 'utf-8')
        self.wr = csv.writer(self.file, dialect="excel")
        self.wr.writerow(['name', 'pub_date', 'city', 'salary'])

    def process_item(self, item, spider):
        self.wr.writerow([item['name'], item['pub_date'], item['city'], item['salary']])
        return item

    def close_spider(self, spider):
        self.file.close()


class JobspiderPipeline_two(object):

    def __init__(self):
        self.file = codecs.open('51job_one_two.csv', 'w', 'utf-8')
        self.wr = csv.writer(self.file, dialect="excel")
        self.wr.writerow(['name', 'pub_date', 'city', 'salary', 'require'])

    def process_item(self, item, spider):
        self.wr.writerow([item['name'], item['pub_date'], item['city'], item['salary'], item['require']])
        return item

    def close_spider(self, spider):
        self.file.close()
