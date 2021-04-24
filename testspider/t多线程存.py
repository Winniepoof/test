import t贴吧图片
import threading

def multi_thread1():
    print('start')
    threads=[]
    for url in t贴吧图片.img_data:
        threads.append(
            threading.Thread(target=t贴吧图片, args=(url,))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('end')

def multi_thread2():
    print('start')
    threads=[]
    for url in t贴吧图片.imgs:
        threads.append(
            threading.Thread(target=t贴吧图片, args=(url,))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('end')


if __name__ == '__main__':
    multi_thread1()
    multi_thread2()

