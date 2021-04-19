import requests
from bs4 import BeautifulSoup

urls=[
    f'https://www.cnblogs.com/#p{i}'
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
    links=soup.find_all('a',class_='post-item-title')
    return [(link['href'],link.get_text()) for link in links]

if __name__ == '__main__':
    for result in parse(craw(urls[0])):
        print(result)