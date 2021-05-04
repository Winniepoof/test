from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
#以下ip使用自己可使用的代理IP
proxy_arr = [
     '--proxy-server=https://111.26.180.102'#111.26.180.102  117.29.242.85
 ]



chrome_options = Options()

proxy = random.choice(proxy_arr)  # 随机选择一个代理
print(proxy) #如果某个代理访问失败,可从proxy_arr中去除

chrome_options.add_argument(proxy)  # 添加代理

browser = webdriver.Chrome()#options=chrome_options

browser.get("http://httpbin.org/ip")

print(browser.page_source)