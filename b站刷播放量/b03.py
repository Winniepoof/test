import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# headers = {
# 'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 'Accept-Encoding':' gzip, deflate, br',
# 'Accept-Language':' zh-CN,zh;q=0.9',
# 'Cache-Control':' max-age=0',
# 'Connection':' keep-alive',
# 'Host':' www.bilibili.com',
# 'Upgrade-Insecure-Requests':' 1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
# }
try:
    chromeOptions = webdriver.ChromeOptions()
    proxy = requests.get('http://127.0.0.1:5010/get/').text #本身维护的代理池并提供接口
    print(proxy)
    chromeOptions.add_argument("--proxy-server=http://{}".format(proxy)) #设置代理
    browser = webdriver.Chrome(options=chromeOptions)#'D:\\Google\\Chrome\\Application\\chromedriver.exe',
    browser.delete_all_cookies()  # 删除cookie
    browser.get("https://www.bilibili.com/video/BV1u4411Q7Xw")
    element = WebDriverWait(browser, 15).until( #等待播放按钮可以被加载而且可以被点击，15s后若是还没加载完成而且不知足被点击的条件，就抛出异常
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bilibiliPlayer"]/div[1]'))
    )
    element.click()
    print(browser.get_cookies())

except Exception as e:
    print('异常'*10)
    print(e)