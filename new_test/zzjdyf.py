import requests
import re
from fake_useragent import UserAgent
import parsel

url='http://www.hnzzj.com/'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers).text
print(response)
print('----------------------------------------------------------')
#解析
html=parsel.Selector(response)
print(html)

# srcs=html.xpath('//div[@class="container clearfix"]//div//ul//li//a/@href').getall()
# print(srcs)
titles=html.xpath('//div[@class="container clearfix"]//div//ul//li//a/text()').getall()
print(titles)
print('--------------------------------------------------------------------------')
hrefs=html.xpath('//div[@class="main pagebox"]//@href').getall()
print(hrefs)
# for href in hrefs:
#     print(href)

furl='http://www.hnzzj.com/'

https = []
wwws = []
for href in hrefs:
    # print(2)
    print(href)
    # print(3)

    if re.search('http',href):
        https.append(href)
    else:
        wwws.append(href)
for http in https:
    print(http)

for www in wwws:
    ur=furl+www
    print('当前地址为',ur)
    #再次请求
    response2=requests.get(ur,headers).text
    html=parsel.Selector(response2)
    srcs = html.xpath('//div[@class="main pagebox"]//img//@src').getall()
    for src in srcs:
        print(src)


# for title in titles:
#
#     print(title)
    #再次请求


# for src in srcs:
#     ur=furl+src
#     print('当前地址为',ur)
#     #再次请求
#     response2=requests.get(ur,headers).text
#
#     f_img=parsel.Selector(response2)
#     texts = html.xpath('//div[@class="e_box p_con"]//span//text()').getall()
#     for text in texts:
#         print(text)
    #再次解析
    # img_data=f_img.xpath('//cc/div/img[@class="BDE_Image"]/@src').getall()
    # print(img_data)

    # for imgs in img_data:
    #     img=requests.get(imgs,headers).content
    #     #保存
    #     filename=imgs.split('/')[-1]
    #     with open('PIC\\'+filename, mode='wb') as f:
    #         f.write(img)
    #         print('正在打印：',filename)