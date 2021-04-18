import test爬虫
import threading
import time

def single_thread():
    print('start')
    for url in test爬虫.urls:
        test爬虫.craw(url)
    print('end')

def multi_thread():
    print('start')
    threads=[]
    for url in test爬虫.urls:
        threads.append(
            threading.Thread(target=test爬虫.craw,args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('end')


if __name__ == '__main__':
    start=time.time()
    single_thread()
    end=time.time()
    print('用了',end-start,'秒')

    start = time.time()
    multi_thread()
    end = time.time()
    print('用了', end - start, '秒')