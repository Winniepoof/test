import urllib.request
from urllib.request import urlopen

url1='http://www.bing.com'

res=urlopen(url1)

info=res.read()

#print(info.decode())

#打印状态码
print(res.getcode)
print('------------------------------------------')
#打真实url
print(res.geturl())
print('------------------------------------------')
#响应头
print(res.info())
