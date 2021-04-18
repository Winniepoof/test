from urllib.request import urlopen
from urllib.request import Request
from fake_useragent import UserAgent
from urllib.parse import quote

url1='http://www.baidu.com/s?wd={}'.format(quote('鲁邦三世thefirst'))

headers={
            'User-Agent':UserAgent().random
}
print('--------------------------------------------')
request=Request(url1,headers=headers)
response=urlopen(request)
print(response.read().decode())


#print(req.get_header('User-agent'))