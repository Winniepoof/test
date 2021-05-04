import requests
import time
import random
#主要是调用B站的API来实现刷播放量
#首先先定义它的headers，在我们点击视频的时候，查看它的xhr，然后我们就可以找到它的对应cookie了，因为怎么获取播放量和cookie有关
headers = {

    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',#'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'origin': 'https://www.bilibili.com',
    'Connection': 'keep-alive',
    'referer': 'https://www.bilibili.com/video/BV1u4411Q7Xw',
    "cookie": "_uuid=1B08AB27-5C0B-E477-1C08-9B25225B4FB442216infoc; buvid3=24D9972A-3808-4BE8-A778-33C2AD07B96753952infoc; rpdid=|(uYmmullJRJ0J'ul)m~|RYml; CURRENT_FNVAL=80; LIVE_BUVID=AUTO5116018050424022; buvid_fp=24D9972A-3808-4BE8-A778-33C2AD07B96753952infoc; SESSDATA=a8541c98%2C1629361087%2Cc52a0%2A21; bili_jct=db92495d12f13bcc28b6a21c7d9f1e6e; DedeUserID=401425662; DedeUserID__ckMd5=610383d5b5d06845; sid=9p121mhm; blackside_state=1; CURRENT_QUALITY=0; fingerprint3=f5c08d3b5948d11826e86bac814005d0; fingerprint=d3407312651e0e65ba636f9f44f77714; fingerprint_s=0f5cfb36874876ce84828d51b92e4b81; buvid_fp_plain=24D9972A-3808-4BE8-A778-33C2AD07B96753952infoc; bp_t_offset_401425662=520600845743032189; bp_video_offset_401425662=520810319889746427; PVID=6; bsource=search_baidu; bfe_id=cade757b9d3229a3973a5d4e9161f3bc",
    #"_uuid=3A318514-7B21-7F9B-715D-5358FA315D0D11914infoc; buvid3=7B7F7CFF-E0CE-4317-AC2C-C8ADF975289253920infoc; sid=9sbfkfld; CURRENT_FNVAL=16; rpdid=|(uYm~YJm))l0J'ul))R)u~YJ; LIVE_BUVID=AUTO6015884836169069; CURRENT_QUALITY=80; bp_t_offset_35906556=392132580010163986; PVID=3; DedeUserID=35906556; DedeUserID__ckMd5=6bc77a6b9c4d788a; SESSDATA=c7a7e24c%2C1605943181%2C95472*51; bili_jct=d263a22829f9bad2b775aa9813ccf5d1; bp_video_offset_35906556=393915923444549998; bfe_id=da609d6ad479671e4cd33f2670c43937",

}
stime = str(int(time.time()))
#获取我们要刷这个视频的data数据
data= {
    'aid':'63325855',
    'cid':'109974192',
    "bvid": "BV1u4411Q7Xw",
    'part':'1',
    'mid':'401425662',
    'lv':'5',
    "stime" :stime,
    'jsonp':'jsonp',
    'type':'3',
    'sub_type':'0',
}

ip_list=['27.159.189.198','49.87.83.231','117.29.242.85']

def get_random_ip(ip_list):
    proxy_list=[]
    for ip in ip_list:
        proxy_list.append('http://'+ip)
    proxy_ip=random.choice(proxy_list)
    proxies={'http':proxy_ip}#proxy_ip
    return proxies

#然后就先是解析这个页面了
def get_html(url,proxies):
    count = 0
    while True:
        try:
            #发起一个post请求，去请求这个页面，从而获得一次点击量
            print(1)
            header={'User-Agent':headers}
            req = requests.get(url,data=data,headers=headers)#post  ,proxies=proxies
            print(2)
            count += 1
            print("now in loop {}".format(count))
            print(req.text)
            #这里设置等待时间，因为B站的时间间隔是400秒的，当然如果你是用IP池的可以随便浪
            #time.sleep(100)
        except Exception as e:
            print(e)
            time.sleep(100)
            print('overs')
    print("over")

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1u4411Q7Xw"
    proxies=get_random_ip(ip_list)
    print(proxies)
    get_html(url,proxies)


