from selenium import webdriver

url=webdriver.Chrome()
url.get('https://account.guokr.com/sign_in/')

botton=url.find_element_by_id('permanent')
botton.click()