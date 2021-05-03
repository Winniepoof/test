import parsel
import requests
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from lxml import etree


url=webdriver.Chrome()
url.get('https://search.bilibili.com/all?keyword=%E5%A5%B3%E5%84%BF%E5%9B%BD%E6%9C%B1%E7%90%B3&from_source=webtop_search&spm_id_from=333.851')

source=url.page_source
print(source)
html_sourse=etree.HTML(source)

v_img=html_sourse.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a/div/div[1]/img/@src')[0]
print('https:'+v_img)



# headers={'UserAgent':UserAgent().chrome}
# response=requests.get(url,headers=headers).text
#print(response)
#print(response)

#html=parsel.Selector(response)
# print(html)
# title=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a/@title').getall()
# ur=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a/@href').getall()
# v_im=html.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/a/div/div[1]/img').getall()
# com=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a/div/div[4]/span[1]/text()')
# playtime=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[3]/span[1]/text()').getall()[0].strip()
# print(title)
# print(ur[0])
# print(v_im)
# print(com)
# print(playtime)
# for t in title:
#     print(t)