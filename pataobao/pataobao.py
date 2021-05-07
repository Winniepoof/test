import parsel
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import lxml

url='https://nanzhuang.tmall.com/?spm=875.7931836/B.category2016011.1.659c42654j078q&acm=lb-zebra-148799-667863.1003.4.708026&scm=1003.4.lb-zebra-148799-667863.OTHER_14561677576501_708026'
header={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers=header).text
#print(response)


soup=BeautifulSoup(response,'lxml')
print(soup)

#items=soup.find_all('li',class_='pc-items-item item-undefined')
items=soup.find_all(class_='item')
print(items)
for item in items:
    print(item)
    #price=item.find('a').get('href')
    title=item.find(class_='itemTitle')
    print(title)
    #print(price)




# html=parsel.Selector(response)
# img = html.xpath('./a[@class="pc-items-item-img img-loaded"]/@src').extract()
#name=html.xpath('//*[@id="mx_5"]/ul/li[1]/a/div[1]/span/text()')#'./a[@class="pc-items-item-title pc-items-item-title-row2"]/@title-text'
# coupon_price=html.xpath('./a[@class="price-con"]/@coupon-price-afterCoupon').extract()
# old_price=html.xpath('./a[@class=""]/@coupon-price-old').extract()
# seller= html.xpath('./a[@class="seller-info"]/@atbfont seller-icon').extract()
# sell_num= html.xpath('./a[@class="item-footer"]/@sell-info').extract()
#adress=()

#print(name)