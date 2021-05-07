import parsel

import requests
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from lxml import etree
from bs4 import BeautifulSoup
import re

url=webdriver.Chrome()
url.get('https://nanzhuang.tmall.com/?spm=875.7931836/B.category2016011.1.659c42654j078q&acm=lb-zebra-148799-667863.1003.4.708026&scm=1003.4.lb-zebra-148799-667863.OTHER_14561677576501_708026')

source=url.page_source
print(source)
#html_sourse=etree.HTML(source)
# v_img=html_sourse.xpath('//*[@id="itemImg1"]')[0]
# print('https:'+v_img)
#source.encoding='utf-8'
#html=source.text
#soup=BeautifulSoup(html,'lxml')
#soup=BeautifulSoup(source,'html.parser')
soup=BeautifulSoup(source,'lxml')
list=soup.find_all(class_='item')#find(class_='all-list').
html_element=etree.HTML(source)
# v_name=html_element.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a')
# for i in v_name:
#     print(i)
for item in list:
    titles=item.find_all(class_='itemTitle')#.get('href')
    prices=item.find(class_='itemPrice')#,'span',class_='priceYang'
    shoptitles=item.find(class_='shopTitle')
    titles=str(titles)
    #title = re.sub(r'>.*?<',"", titles)#输出<>之间的内容
    title_list = re.findall('[\u4e00-\u9fa5]',titles)
    title=''.join(title_list)
    print(title)
    prices=str(prices)
    price=1
    #print(price)
    shoptitles=str(shoptitles)
    shoptitle_list=re.findall('[\u4e00-\u9fa5]',shoptitles)
    shoptitle=''.join(shoptitle_list)
    print(shoptitle)

url.close()
url.quit()