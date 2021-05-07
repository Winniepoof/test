import b02
import threading

def multi_b():
    print('start')
    threads=[]
    for i in range(3):
        url="https://www.bilibili.com/video/BV1u4411Q7Xw"
        threads.append(
            threading.Thread(target=b02.bil_views,args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('end')

if __name__ == '__main__':
    multi_b()
