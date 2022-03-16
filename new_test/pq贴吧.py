from pyquery import PyQuery as pq
import requests
import re
from fake_useragent import UserAgent
import parsel


url='https://tieba.baidu.com/f?kw=%CA%AF%D4%AD%C0%EF%C3%C0&fr=ala0&loc=rec'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers).text
print(response)
print('-------------------------------------------------------------------------')
doc=pq(response)
print(doc)
print('-----------------------------------------------------------')
titles=doc('title').items()
print(titles)
for title in titles:
    print(title)

print('-----------------------------------------------------')

srcs=doc('src').items()
print(srcs)
for src in srcs:
    print(src)

