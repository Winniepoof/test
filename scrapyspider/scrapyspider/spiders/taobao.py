# import sys
# sys.path.append("..")
import scrapy
# from scrapyspider.scrapyspider.items import ScrapyspiderItem
from ..items import ScrapyspiderItem

#scrapy crawl clothes

class taobao(scrapy.Spider):
    name='clothes'
    allowed=['taobao.com']
    start_urls=['https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E5%A5%B3%E8%A3%85&clk1=47577b64c9afa844e095a9ff765a0547&upsId=47577b64c9afa844e095a9ff765a0547']

    def parse(self,response):
        clothes=response.xpath('//u1[@class="pc-items-item item-undefined"]/li')
        print(clothes)
        for clothe in clothes:
            item=ScrapyspiderItem()
            item['name']=clothe.xpath('./a[@class="pc-items-item-title pc-items-item-title-row2"]/@title-text').extract()
            item['coupon_price']=clothe.xpath('./a[@class="price-con"]/@coupon-price-afterCoupon').extract()
            item['old_price']=clothe.xpath('./a[@class=""]/@coupon-price-old').extract()
            item['seller'] = clothe.xpath('./a[@class="seller-info"]/@atbfont seller-icon').extract()
            item['sell_num'] = clothe.xpath('./a[@class="item-footer"]/@sell-info').extract()
            item['img'] = clothe.xpath('./a[@class="pc-items-item-img img-loaded"]/@src').extract()

            yield item