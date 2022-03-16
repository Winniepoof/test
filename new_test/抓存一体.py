import requests
import re
from fake_useragent import UserAgent
import parsel
import mysql_inport_data
import pipline



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

    for src in srcs:
        print(src)
        pipline.process_item(src)