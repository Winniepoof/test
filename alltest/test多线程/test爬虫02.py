import requests
from bs4 import BeautifulSoup

urls=[
    f'https://tieba.baidu.com/f?kw=%E7%9F%B3%E5%8E%9F%E9%87%8C%E7%BE%8E&ie=utf-8&pn={50*i}'
    for i in range(0,10)
]

#print(urls)
def craw(url):
    r=requests.get(url)
    return r.text
    #print(url,len(r.text))

def parse(html):
    #class='post-item-title'
    soup=BeautifulSoup(html,'html.parser')
    links=soup.find_all('a',class_=('j_th_tit'))#class_='post-item-title'rel_='noreferrer',
    return [(link['href'],link.get_text()) for link in links]

if __name__ == '__main__':
    for result in parse(craw(urls[0])):
        print(result)