from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

url=webdriver.Chrome()
url.get('http://www.bilibili.com/')

wait=WebDriverWait(url,10)
input=wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"banner_link > div > div > form > input")))
wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="banner_link"]/div/div/form/button')))

input.send('女儿国朱琳')