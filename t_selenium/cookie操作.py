from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url=webdriver.Chrome()
url.get('https://www.baidu.com')

for cookie in url.get_cookies():
    print('='*30)

print({cookie['name']:cookie['value'] for cookie in url.get_cookies()})

print(url.get_cookie('BD_UPN'))

url.delete_cookie('BD_UPN')

url.delete_all_cookies()