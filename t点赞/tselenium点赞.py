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
    #'111.26.180.82',
    'https://111.26.180.82',
    # 'https://103.121.210.84',
    # 'https://36.56.101.120',
    # 'https://114.233.171.250',
    # 'https://49.85.188.222',
    # 'https://1.70.67.20',
    # 'https://114.98.173.85',
    # 'https://49.85.188.242',
    #'https://117.64.236.75',
    # 'https://27.156.197.102',
    # 'https://121.226.215.247',
    # 'https://180.119.95.119',
    # 'https://49.85.188.222',
    # 'https://61.130.194.136',
    # 'https://1.70.67.86'
 ]

#chrome_options =Options()
chrome_options=webdriver.ChromeOptions()
#proxy = random.choice(proxy_arr)  # 随机选择一个代理
#print(proxy) #如果某个代理访问失败,可从proxy_arr中去除



def bz(i):
    #time.sleep(10)
    #chrome_options.add_argument("--proxy-server={}".format(i))  # 添加代理
    chrome_options.add_argument(i)
    browser = webdriver.Chrome(options=chrome_options)  # options=chrome_options
    print(i)
    browser.delete_all_cookies()
    browser.get("http://162065568784.brief.meijingchangyou.com/app/vote.index-461.jsp?aid=6a380a071eb3edf15ee580acf6851bd5&dgroupsid=0&time=1620655687")
    #time.sleep(5)
    Wait = WebDriverWait(browser, 100)

    botton = Wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list_box"]/li[10]/img"]/div/button')))
    botton.click()
    #player = Wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list_box"]/li[10]/div[2]/button')))
    #player.click()
    #print(browser.get_cookies())

    # time.sleep(5)
    # browser.close()
    # browser.quit()


# for i in proxy_arr:
#     testip(i)
#     print(2)
#     #bz(i)