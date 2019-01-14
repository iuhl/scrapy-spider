import scrapy

from firstScrapy.items import AutoHomeItem


class AutoHomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['autohome.com','autohome.com.cn']

    # 所有车型
    start_urls = ['https://www.autohome.com.cn/grade/carhtml/A.html']

    def parse(self, response):
        initial_list_ids = response.xpath("//body/dl/@id").extract()
        for model_id in initial_list_ids:

            # 品牌
            brand_list = AutoHomeItem()
            brand_list['brand_img'] = 'https:' + response.xpath("//*[@id='"+model_id+"']/dt/a/img/@src").extract_first()
            brand_list['brand_url'] = 'https:' + response.xpath("//*[@id='"+model_id+"']/dt/a/@href").extract_first()
            brand_list['brand_name'] = response.xpath("//*[@id='"+model_id+"']/dt/div/a/text()").extract_first()

            # 经销商
            i = j = 1
            brand_dealers = []
            dealer_name = response.xpath("//*[@id='"+model_id+"']/dd/div[" + str(i) + "]/a/text()").extract_first()
            while dealer_name is not None:
                dealer_list = AutoHomeItem().dealerItem()
                # 汽车型号
                model_car_ids=response.xpath("//*[@id='"+model_id+"']/dd/ul["+str(j)+"]/li/@id").extract()
                dealer_model_car = []
                for model_car_id in model_car_ids:
                    model_car_list = AutoHomeItem().dealerItem().modelItem()
                    model_car_list['model_url']="http:"+response.xpath("//*[@id='"+model_car_id+"']/h4/a/@href").extract_first()
                    model_car_list['model_name'] = response.xpath("//*[@id='"+model_car_id+"']/h4/a/text()").extract_first()

                    if response.xpath("//*[@id='" + model_car_id + "']/text()").extract()[1].strip() != '指导价：暂无':
                        model_car_list['model_price_section'] = response.xpath(
                            "//*[@id='" + model_car_id + "']/div[1]/text()").extract_first()
                        model_car_list['model_price_section'] = model_car_list['model_price_section']\
                                                                +response.xpath("//*[@id='"+model_car_id+"']/div[1]/a/text()").extract_first()
                    else:
                        model_car_list['model_price_section']= '指导价：暂无'

                    model_car_list['model_label']= response.xpath("//*[@id='"+model_car_id+"']/h4/i/@title").extract_first()
                    dealer_model_car.append(model_car_list)

                i = i + 2
                j = j + 1
                dealer_list['brand_dealer'] = dealer_name
                dealer_name = response.xpath("//*[@id='"+model_id+"']/dd/div[" + str(i) + "]/a/text()").extract_first()
                dealer_list['model_items'] = dealer_model_car
                brand_dealers.append(dealer_list)

            brand_list['brand_dealers'] = brand_dealers

            yield brand_list

        bz =[chr(i)for i in range(ord("B"), ord("Z") + 1)]
        for letter in bz:
            yield scrapy.Request("https://www.autohome.com.cn/grade/carhtml/"+letter+".html",callback=self.parse,dont_filter=True)




