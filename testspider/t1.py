import requests
import re

url='https://tieba.baidu.com/f?kw=%CA%AF%D4%AD%C0%EF%C3%C0&fr=ala0&loc=rec'
page=requests.get(url).text
print(page)
res=re.compile(r'src="(https://tiebapic.baidu.com/.+?.jpg)"')
reg=re.findall(res,page)
print(reg)