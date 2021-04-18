

from urllib.request import urlopen
from urllib.request import Request
from fake_useragent import UserAgent

url1='http://www.baidu.com'
ua=UserAgent()

headers={
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
            'User-Agent':ua.chrome
}
print('--------------------------------------------')
print(ua.chrome)

request=Request(url1,headers=headers)
#print(req.get_header('User-agent'))

response=urlopen(url1)

info=response.read()

print(info.decode())


