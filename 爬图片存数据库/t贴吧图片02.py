import requests
import re
from fake_useragent import UserAgent
import parsel
import pipelines

url='https://tieba.baidu.com/f?kw=%CA%AF%D4%AD%C0%EF%C3%C0&fr=ala0&loc=rec'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers).text
#print(response)

#解析
html=parsel.Selector(response)
print(html)
title=html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').getall()
print(title)

#拼接
furl='https://tieba.baidu.com'


for tit in title:
    ur=furl+tit
    #print('当前地址为',ur)
    #再次请求
    response2=requests.get(ur,headers).text

    f_img=parsel.Selector(response2)
    #再次解析
    img_data=f_img.xpath('//cc/div/img[@class="BDE_Image"]/@src').getall()
    print(img_data)

    for data in img_data:
        print(data)
        pipelines.process_item(data)