import parsel
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


url='https://search.bilibili.com/all?keyword=%E5%A5%B3%E5%84%BF%E5%9B%BD%E6%9C%B1%E7%90%B3&from_source=webtop_search&spm_id_from=333.851'
headers={'UserAgent':UserAgent().chrome}
response=requests.get(url,headers=headers).text
#print(response)
#print(response)
#html=parsel.Selector(response)
#print(html)

soup=BeautifulSoup(response,'lxml')
#print(soup)
videos=soup.find_all('li',class_='video-item matrix')
print(videos)

for video in videos:
    title=video.find('a').get('title')
    url=video.find('a').get('href')
    img=video.find('a').get('src')
    print(title)
    print(url)
    print(img)



# title=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a/@title').getall()
# ur=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a/@href').getall()
# v_im=html.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/a/div/div[1]/img').getall()
# com=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a/div/div[4]/span[1]/text()')
# playtime=html.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[3]/span[1]/text()').getall()[0].strip()
# print(title)
# print(ur[0])
# print(v_im)
# print(com)
# print(playtime)
# for t in title:
#     print(t)