# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    coupon_price = scrapy.Field()
    old_price = scrapy.Field()
    seller = scrapy.Field()
    sell_num= scrapy.Field()
    img = scrapy.Field()