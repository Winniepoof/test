from selenium import webdriver
from pyquery import PyQuery as pq


url=webdriver.Chrome()
url.get('https://tieba.baidu.com/f?kw=%CA%AF%D4%AD%C0%EF%C3%C0&fr=ala0&loc=rec')
html=url.page_source
print(html)
print('----------------------------------------------------')
doc=pq(html)
print(doc)

titles=doc('title').text()
print(titles)
for title in titles:
    print(title)


url.close()
url.quit()