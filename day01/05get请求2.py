from urllib.request import urlopen
from urllib.request import Request
from fake_useragent import UserAgent
from urllib.parse import urlencode

arg={
    'wd':'鲁邦三世thefirst',
    'ie':'utf-8'
}

url1='https://www.baidu.com/s?{}'.format(urlencode(arg))
print(url1)

headers={
            'User-Agent':UserAgent().random
}
print('--------------------------------------------')


request=Request(url1,headers=headers)
#print(req.get_header('User-agent'))

response=urlopen(request)

info=response.read()

print(info.decode())