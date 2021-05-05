import 用selenium
import threading

def multi_b():
    print('start')
    threads=[]
    p=[]
    for ip in 用selenium.proxy_arr:
        threads.append(
            threading.Thread(target=用selenium.bz,args=(ip,))
        )
        p.append(
            threading.Thread(target=用selenium.bz, args=(ip,))
        )

    for thread in threads:
        thread.start()
    for a in p:
        a.start()

    for thread in threads:
        thread.join()
    for a in p:
        a.join()

    print('end')

if __name__ == '__main__':
    multi_b()
