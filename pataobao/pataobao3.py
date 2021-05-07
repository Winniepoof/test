from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pyquery import PyQuery as pq
from time import sleep

url=webdriver.Chrome()
url.get('https://nanzhuang.tmall.com/?spm=875.7931836/B.category2016011.1.659c42654j078q&acm=lb-zebra-148799-667863.1003.4.708026&scm=1003.4.lb-zebra-148799-667863.OTHER_14561677576501_708026')

wait=WebDriverWait(url,10)
#good_total =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_ItemList > div.product > div.product-iWrap')))

source=url.page_source
#print(source)
doc=pq(source)
#print(doc)
good_items=doc('#J_ItemList .product').items()
#print(good_items)
for item in good_items:
    print(item)
    # good_title = item.find('itemTitle').text().replace('\n', "").replace('\r', "")
    # good_status = item.find('.productStatus').text().replace(" ", "").replace("笔", "").replace('\n', "").replace('\r',                                                                                                                 "")
    # good_price = item.find('.productPrice').text().replace("¥", "").replace(" ", "").replace('\n', "").replace('\r', "")
    # good_url = item.find('.productImg').attr('href')
    # #print(good_title + "   " + good_status + "   " + good_price + "   " + good_url + '\n')
    # print(good_title)
    # print(good_status)
    # print(good_price)

# url.close()
# url.quit()