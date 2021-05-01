from selenium import webdriver
from selenium.webdriver.support.ui import Select

url=webdriver.Chrome()
url.get('http://www.dobai.cn')

selectbt=Select(url.find_element_by_name('jumpMenu'))
selectbt.deselect_all()
