from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import csv


url=webdriver.Chrome()
url.get('https://cn.investing.com/crypto/bitcoin/btc-usd-historical-data')
#time.sleep(10)
element = WebDriverWait(url, 15).until(  # 等待播放按钮可以被加载而且可以被点击，15s后若是还没加载完成而且不知足被点击的条件，就抛出异常
    EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
)
element.click()
source=url.page_source
print(source)
html_sourse=etree.HTML(source)

c=html_sourse.xpath("//div[@id='results_box']//table")
print(c)

zcry_table = etree.tostring(c[0], encoding='utf-8').decode()
df = pd.read_html(zcry_table, encoding='utf-8', header=0)[0]
results = list(df.T.to_dict().values())   # 转换成列表嵌套字典的格式
print(results)

for result in results:
    date = result['日期']
    close_p = result['收盘']
    open_p = result['开盘']
    high = result['高']
    low = result['低']
    vol = result['交易量']
    range_of_increase = result['涨跌幅']
    print(date, close_p, open_p, high, low, vol,range_of_increase)

    f = open('bits.csv', 'wb')
    #f.write('\xEF\xBB\xBF')
    writer = csv.writer(f)
    writer.writerow(date, close_p, open_p, high, low, vol,range_of_increase)

# def getSortedValues(row):
#     sortedValues=[]#初始化为空list
#     keys=row.keys()
#     keys.sort()
#     for key in keys:
#         sortedValues.append(row[key])
#     return sortedValues
#
# f=open('bits.csv','wb')
# f.write('\xEF\xBB\xBF')
# writer=csv.writer(f)
# #heads=result
# sortedValues = getSortedValues(result)
# #writerow()方法是一行一行写入，
# #writerows方法是一次写入多行
# writer.writerow(sortedValues)
#
# for row in result:
#     sortedValues = getSortedValues(row)
#     print (sortedValues)
#     writer.writerow(sortedValues)

# with open("bits.csv", 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['d'])
#     for i in range(len(result)):
#         writer.writerow([result[i][1], result[i][2],result[i][3],result[i][4], result[i][5]])
time.sleep(6)
url.close()
url.quit()