import pymysql
import sqlite3
db=sqlite3.connect('d:/GitHub/testspider.db')
cur=db.cursor()

sql='select *from url'



try :
    cur.execute(sql)
    urls = cur.fetchall()
    #print(person_all)
    for url in urls:
        print(url)
except Exception as e:
    print(e)
    db.rollback()
    print('查询失败')
finally:
    cur.close()
    db.close()