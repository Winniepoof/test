from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
#以下ip使用自己可使用的代理IP
#--proxy-server=  111.26.180.102  117.29.242.85  103.121.210.84
proxy_arr = [
    'https://103.121.210.84',
    'https://36.56.101.120',
    'https://114.233.171.250',
    'https://49.85.188.222',
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

chrome_options = Options()

#proxy = random.choice(proxy_arr)  # 随机选择一个代理
#print(proxy) #如果某个代理访问失败,可从proxy_arr中去除

def testip(i):
    print(i)
    chrome_options.add_argument(i)  # 添加代理
    browser = webdriver.Chrome(options=chrome_options)  # options=chrome_options
    browser.get('http://httpbin.org/ip')
    print(browser.page_source)
    browser.close()


def bz(i):
    #time.sleep(10)
    chrome_options.add_argument(i)  # 添加代理
    browser = webdriver.Chrome(options=chrome_options)  # options=chrome_options
    print(i)
    browser.get("https://www.bilibili.com/video/BV1u4411Q7Xw")
    time.sleep(5)
    Wait = WebDriverWait(browser, 100)
    player = Wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bilibiliPlayer"]/div[1]')))
    #ti=Wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="viewbox_report"]/h1/span')))
    player.click()
    # time.sleep(5)
    # ti.click()
    time.sleep(2)
    browser.close()
    #time.sleep(5)


# for i in proxy_arr:
#     testip(i)
#     print(2)
#     bz(i)