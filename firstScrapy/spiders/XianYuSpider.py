import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class XianYuSpider(scrapy.Spider):
    name="xianyu"
    allowed_domains=["taobao.com"]

    start_urls=[
        "https://2.taobao.com/"]

    def parse(self, response):
        unicode_body=response.body_as_unicode()
        print(unicode_body)
        # goods_list=response.xpath("//div[@class='item-list-wrap']/a")
        # for goods in goods_list:
        #     print(goods)
