import requests
import re
from fake_useragent import UserAgent
import parsel

url='https://cn.investing.com/crypto/bitcoin-cash/bch-btc-historical-data?cid=1090717'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers).text
print(response)

#解析
html=parsel.Selector(response)
print(html)
title=html.xpath('//div[@class="genTbl closedTbl historicalTbl"]/div/a/@href').getall()
print(title)

#拼接
# furl='https://tieba.baidu.com'
#
#
# for tit in title:
#     ur=furl+tit
#     #print('当前地址为',ur)
#     #再次请求
#     response2=requests.get(ur,headers).text
#
#     f_img=parsel.Selector(response2)
#     #再次解析
#     img_data=f_img.xpath('//cc/div/img[@class="BDE_Image"]/@src').getall()
#     print(img_data)
#
#     for imgs in img_data:
#         img=requests.get(imgs,headers).content
#         #保存
#         filename=imgs.split('/')[-1]
#         with open('PIC\\'+filename, mode='wb') as f:
#             f.write(img)
#             print('正在打印：',filename)