# -*- coding: utf-8 -*-
import scrapy
from ..items import JobrequireItem, JobspiderItem
from scrapy.http.request import Request


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['51job.com']
    page = 1
    url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,{0}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    start_urls = [url.format(page)]

    def parse(self, response):
        # print(response.body)
        job_list = response.xpath("//div[@class='dw_table']/div[@class='el']")
        for each in job_list:
            name = each.xpath("normalize-space(./p/span/a/text())").extract()[0]
            city = each.xpath("./span[@class='t3']/text()").extract()[0]
            pub_date = each.xpath(".//span[@class='t5']/text()").extract()[0]
            salary = each.xpath(".//span[@class='t4']/text()").extract()
            if len(salary) > 0:
                salary = salary[0]
            else:
                salary = ''
            sec_url = each.xpath("normalize-space(./p/span/a/@href)").extract()[0]
            item = JobspiderItem()
            item['name'] = name
            item['city'] = city
            item['pub_date'] = pub_date
            item['salary'] = salary
            # 将获取的数据交给pipeline
            yield item
            yield Request(sec_url, callback=self.sec_parse, meta={"item": item})

    def sec_parse(self, response):
        info = response.xpath('//p[@class="msg ltype"]/@title').extract()
        if len(info) != 0:
            item = JobrequireItem()
            item['name'] = response.meta['item']['name']
            item['city'] = response.meta['item']['city']
            item['pub_date'] = response.meta['item']['pub_date']
            item['salary'] = response.meta['item']['salary']
            item["require"] = info[0].replace('\xa0\xa0', '')
            yield item
