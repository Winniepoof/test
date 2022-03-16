import requests
import re
from fake_useragent import UserAgent
import parsel

url='https://tieba.baidu.com/f?kw=%CA%AF%D4%AD%C0%EF%C3%C0&fr=ala0&loc=rec'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers).text
print(response)

#解析
html=parsel.Selector(response)
print(html)
title=html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').getall()
#//*[@id="thread_top_list"]/li[1]/div/div[2]/div/div[1]/a
#//*[@id="thread_top_list"]/li[2]/div/div[2]/div/div[1]/a
title1=html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/div/a/@title').getall()
#//*[@id="thread_list"]/li[3]/div/div[2]/div[1]/div[1]
print(title)
# print(title1)

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

    # for imgs in img_data:
    #     img=requests.get(imgs,headers).content
    #     #保存
    #     filename=imgs.split('/')[-1]
    #     with open('PIC\\'+filename, mode='wb') as f:
    #         f.write(img)
    #         print('正在打印：',filename)