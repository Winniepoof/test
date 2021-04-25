import t贴吧图片02
import threading

def multi_thread1():
    print('start')
    threads=[]
    for url in t贴吧图片02.img_data:
        threads.append(
            threading.Thread(target=t贴吧图片02, args=(url,))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('end')