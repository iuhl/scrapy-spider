# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstscrapyItem(scrapy.Item):
    sequence_number = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()
    star_level = scrapy.Field()
    pass


class XianYuItem(scrapy.Item):
    sequence_number = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()
    star_level = scrapy.Field()
    pass


# 汽车之家
class AutoHomeItem(scrapy.Item):
    # 品牌
    brand_name = scrapy.Field()
    brand_img = scrapy.Field()
    brand_url = scrapy.Field()
    # 品牌 经销商
    brand_dealers = scrapy.Field()

    pass

    # 品牌 经销商
    class dealerItem(scrapy.Item):
        brand_dealer = scrapy.Field()
        model_items = scrapy.Field()
        pass

        # 型号
        class modelItem(scrapy.Item):
            model_name = scrapy.Field()
            model_url = scrapy.Field()
            model_price_section = scrapy.Field()
            model_price_url = scrapy.Field()
            model_picture_url = scrapy.Field()
            model_used_car_url = scrapy.Field()
            model_forum_url = scrapy.Field()
            model_WoM_url = scrapy.Field()
            # 标签
            model_label = scrapy.Field()
            pass

