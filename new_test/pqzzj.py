import re

from selenium import webdriver
from pyquery import PyQuery as pq
import time
import re

url=webdriver.Chrome()
url.get('http://www.hnzzj.com/intro/21.html')
#http://www.hnzzj.com/intro/21.html
#wait=WebDriverWait(url,10)##mx_5 > ul > li:nth-child(1) #innerSearchGoodList > div:nth-child(2)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#innerSearchGoodList > div>div')))
time.sleep(2)
html = url.page_source
doc = pq(html)
print(doc)##innerSearchGoodList > div:nth-child(2) > div:nth-child(2)
print('----------------------------------------------------------------------------------------------')
print (doc.text())
items=doc('data_analyse-ename').items()
##innerSearchGoodList > div>div
#//*[@id="c_portalResIntro_category-15605002629503772"]/div/div/div[2]/div[2]/div[1]/a
print(items)
#//*[@id="w_fimg-1558506245754"]/div/div/a/div/img
for item in items:
    # print(2)
    print(item)
    # print(3)
    good=[]
    title= item.find('.title').text()
    good.append(str(title))
    # price=item.find('.itemPrice').text()
    # good.append(str(price))
    # shop=item.find('.shopTitle').text()
    # good.append(str(shop))
    # imgs=item.find('.itemCover').attr('style')
    # imgs=str(imgs)
    # a = re.compile("'(.*)'")
    # img=a.findall(imgs)
    # img=''.join(img)
    # img='https:'+img
    # good.append(img)
    #
    # print(img)
print(good)


time.sleep(2)
url.close()
url.quit()