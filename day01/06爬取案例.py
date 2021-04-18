from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent


def get_html(url):

    headers={
        'User-Agent':UserAgent().chrome
    }
    request=Request(url,headers=headers)
    response=urlopen(request)
    print(response.read().decode())
    return response.read()


def save_html(filename,a):
        f=open(filename,'wb')
        f.write(a)
        



def main ():
    content=input('请输入下载内容:')
    num=input('请输入下载多少页:')
    base_url1='https://tieba.baidu.com/f?ie=utf-8&{}'
    for pn in range(int(num)):
        args={
            'pn':pn*50,
            'kw':content
        }
        filename = '第' + str(pn+1) + '页.html'
        args=urlencode(args)
        print('正在下载'+filename)
        b=get_html(base_url1.format(args))
        save_html(filename,b)
        #print(base_url1.format(args))
        #get_html('https://tieba.baidu.com/f?ie=utf-8&kw=%E7%9F%B3%E5%8E%9F%E9%87%8C%E7%BE%8E&fr=search')

if __name__ == '__main__':
    main()
