import parsel
import requests
from fake_useragent import UserAgent

url='https://search.bilibili.com/all?keyword=%E5%A5%B3%E5%84%BF%E5%9B%BD%E6%9C%B1%E7%90%B3&from_source=webtop_search&spm_id_from=333.851'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers=headers).text
#print(response)
html=parsel.Selector(response)
print(html)
title=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a/@title').getall()
ur=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a/@href').getall()
v_im=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a/div/div[1]/img').get('src')
com=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a/div/div[4]/span[1]/text()')
playtime=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[3]/span[1]/text()').getall()[0].strip()
print(title)
print(ur[0])
print(v_im)
print(com)
print(playtime)
# for t in title:
#     print(t)