# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AngelItem
from scrapy.pipelines.images import ImagesPipeline

class AngelspiderSpider(CrawlSpider):
    name = 'angelspider'
    allowed_domains = ['angelimg.com']
    start_urls = ['http://www.angelimg.com/']
    # start_urls = ['http://www.angelimg.com/ang/1440']
    rules = (
        # Rule(LinkExtractor(allow=r'http://www.angelimg.com/index/\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/ang/\d+/\d+'), callback='parse_item', follow=True),    #图集翻页
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/ang/\d+'), follow=True),                               #图片翻页
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/index/\d+'),  follow=True),                            #首页
    )

    def parse_item(self, response):
        item=AngelItem()
        item['image_urls']=response.xpath('.//div[@id="content"]/a/img/@src').extract()
        # print(item,'-------------------------')
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
