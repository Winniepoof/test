from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

# 基本配置

# chrome_options=Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--no-gpu')
# chrome_options.add_argument('--disable-setuid-sandbox')
# chrome_options.add_argument('--single-process')
# chrome_options.add_argument('--window-size=1920,1080')

USER_AGENT = [
    'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
]

proxy_arr = [
    'https://153.36.134.220',
    # 'https://111.26.180.82',
    # 'https://103.121.210.84',
    # 'https://36.56.101.120',
    # 'https://114.233.171.250',
    # 'https://49.85.188.222',
    # 'https://1.70.67.20',
    # 'https://114.98.173.85',
    # 'https://49.85.188.242',
    # 'https://117.64.236.75',
    # 'https://27.156.197.102',
    # 'https://121.226.215.247',
    # 'https://180.119.95.119',
    # 'https://49.85.188.222',
    # 'https://61.130.194.136',
    # 'https://1.70.67.86'
 ]

# 参数 url 为B站视频的链接
def bil_views(url):
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    ua = random.choice(USER_AGENT)
    ip=random.choice(proxy_arr)
    chrome_options.add_argument('--user-agent=%s' %ua)#'--user-agent=%s' %ua,"--proxy-server=%s" %ip

    # 代码
    browser = webdriver.Chrome(options=chrome_options)

    # 访问网页
    browser.get(url)
    #browser.save_screenshot("1.png")
    time.sleep(6)

    # 根据 id 获取播放按钮
    try:
        path = '//*[@id="bilibiliPlayer"]/div[1]'
        browser.find_element_by_xpath(path)
        time.sleep(1)
        print('控件抓取成功1')
    except Exception:
        try:
            path = '//*[@id="bilibiliPlayer"]/p[1]/p[1]/p[9]/p[2]/p[2]/p[1]/p[1]/button[1]'
            browser.find_element_by_xpath(path)
            time.sleep(1)
            print('控件抓取成功2')
        except Exception:
            path = '//*[@id="bilibiliPlayer"]/p[1]/p[1]/p[9]/video'
            browser.find_element_by_xpath(path)
            time.sleep(1)
            print('控件抓取成功3')

    # 2倍速播放
    js_2 = '''document.querySelector('video').playbackRate=2'''
    browser.execute_script(js_2)  # 执行js的方法
    # 播放
    browser.find_element_by_xpath(path).click()
    print('播放成功')
    # 睡眠，播放随机一段时间
    view_time = [i for i in range(11, 15)]
    time.sleep(random.choice(view_time))
    # 截图，退出
    #browser.save_screenshot("click1.png")
    browser.close()  # 关闭当前页面
    browser.quit()  # 关闭浏览器


if __name__ == "__main__":
    # 播放100次
    for i in range(5):
        bil_views("https://www.bilibili.com/video/BV1oh411m7ad/")