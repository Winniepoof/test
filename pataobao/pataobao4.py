import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from config import *
from pymongo import MongoClient
import pipline
import time
import re

url=webdriver.Chrome()
url.get('https://nanzhuang.tmall.com/?spm=875.7931836/B.category2016011.1.5cc14265ABwt41&acm=lb-zebra-148799-667863.1003.4.708026&scm=1003.4.lb-zebra-148799-667863.OTHER_14561677576501_708026')

#wait=WebDriverWait(url,10)##mx_5 > ul > li:nth-child(1) #innerSearchGoodList > div:nth-child(2)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#innerSearchGoodList > div>div')))
time.sleep(6)
html = url.page_source
doc = pq(html)
print(doc)##innerSearchGoodList > div:nth-child(2) > div:nth-child(2)
##innerSearchGoodList > div:nth-child(2)
##innerSearchGoodList > div:nth-child(8)
#  //*[@id="innerSearchGoodList"]/div[2]
##innerSearchGoodList
##innerSearchGoodList > div:nth-child(6) > div:nth-child(10)
##innerSearchGoodList > div:nth-child(8) > div:nth-child(10)
items=doc('#innerSearchGoodList > div>div').items()
print(items)

for item in items:
    # print(2)
    print(item)
    # print(3)
    good=[]
    title= item.find('.itemTitle').text()
    good.append(str(title))
    price=item.find('.itemPrice').text()
    good.append(str(price))
    shop=item.find('.shopTitle').text()
    good.append(str(shop))
    imgs=item.find('.itemCover').attr('style')
    imgs=str(imgs)
    a = re.compile("'(.*)'")
    img=a.findall(imgs)
    img=''.join(img)
    img='https:'+img
    good.append(img)
    #img = re.sub(r"/\((.+?)\)/g", "", imgs)
    # p1 = re.compile(r"[(](.*?)[)]", re.S)
    # img_l=re.findall(p1,imgs)
    # img=''.join(img_l)
    # img=str(img)

    # a=img[1]
    # print(a)
    # print(title)
    # print(price)
    # print(shop)
    #print(good)
    print(img)
    # product = {
    #     'title': item.find('.itemTitle').text(),
    #     #'detial_url': item.find('.title .J_ClickStat').attr('href'),
    #     'price': item.find('.itemPrice').text(),
    #     #'deal': item.find('.deal-cnt').text()[:-3],
    #     'shop': item.find('.shopTitle').text(),
    #     #'location': item.find('.location').text(),
    # }
    #print(product)
    #print(len(good[0]))
    if len(good[0])!=0:
        pipline.savesql(good)
    else:
        continue



url.close()
url.quit()