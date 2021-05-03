from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from lxml import etree

urlS=webdriver.Chrome()
urlS.get('http://www.bilibili.com/')

p=urlS.current_url
print(p)

Wait=WebDriverWait(urlS,10)

inputs=Wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav_searchform"]/input')))
botton=Wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nav_searchform"]/div/button')))
index = Wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav_searchform"]/input')))

index.click()
inputs.send_keys('女儿国朱琳')
botton.click()

all_w=urlS.window_handles
urlS.switch_to.window(all_w[1])
u=urlS.page_source
print(u)

total_page=Wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="all-list"]/div[1]/div[3]/div/ul/li[8]/button')))
print(total_page.text)

'''
使用beautifulsoup解析'''

soup=BeautifulSoup(u,'lxml')
list=soup.find_all(class_='info')#find(class_='all-list').
html_element=etree.HTML(u)
# v_name=html_element.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a')
# for i in v_name:
#     print(i)
for item in list:
    title=item.find('a').get('title')
    #url=item.find('a').get('href')
    #img=html_element.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a/div/div[1]/img/@src')[0]
    play_number=item.find('i',class_='icon-playtime')#//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[3]/span[1]/text()
    #play_time=html_element.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[3]/span[1]/text()')[0].strip()
    print(play_number.get_text())
    #print(play_time)
    print(title)
    #print('https:'+url)
    #print('https:'+img)


