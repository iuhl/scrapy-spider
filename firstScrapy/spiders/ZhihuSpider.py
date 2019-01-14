import scrapy;


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']

    start_urls = ['https://www.zhihu.com']

    def parse(self, response):
        unicode_body = response.body_as_unicode()
        print(unicode_body)
