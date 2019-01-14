import scrapy

from firstScrapy.items import FirstscrapyItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/top250"
    ]



    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        movie_list = response.xpath("//ol[@class='grid_view']/li")

        for i_moive in movie_list:
            items = FirstscrapyItem()
            items["sequence_number"] = i_moive.xpath(".//div[@class='item']//em/text()").extract_first()
            items["title"] = i_moive.xpath(".//div[@class='item']//span[@class='title']/text()").extract_first()
            items["desc"] = i_moive.xpath(".//div[@class='bd']//span[@class='inq']/text()").extract_first()
            items["link"] = i_moive.xpath(".//div[@class='hd']//a/@href").extract_first()
            items["star_level"] = i_moive.xpath(".//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            yield items

        next_page = response.xpath("//a[contains(text(),'后页>')]/@href").extract()
        if next_page:
            next_page = next_page[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_page, callback=self.parse)

