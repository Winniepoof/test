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
    #再次解析//*[@id="post_content_139079422988"]/img[4]
    #/html/body/div[4]/div/div/div[2]/div/div[4]/div[1]/div[3]/div/div[3]/div[1]/cc/div[2]/img[4]
    img_data=f_img.xpath('//cc/div/img[@class="BDE_Image"]/@src').getall()
    imgd=f_img.xpath('//*[@id="post_content_139079422988"]/img[4]/@src').getall()
    print(imgd)
    # print(img_data)
    #
    # for data_analyse in img_data:
    #     print(data_analyse)
    #     pipelines.process_item(data_analyse)