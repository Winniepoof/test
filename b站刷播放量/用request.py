import requests
import re
from fake_useragent import UserAgent
import parsel

url='https://www.bilibili.com/video/BV1u4411Q7Xw'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers).text
print(response)
