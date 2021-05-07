import sqlite3
import pymysql

con=sqlite3.connect('d:/GitHub/tspider.db')
#print(con)
cur=con.cursor()#游标对象

sql='''create table good(  
        g_on INTEGER primary key autoincrement,     
        g_title VARCHAR not null,
        g_price VARCHAR not null,
        g_shop VARCHAR not null,
        g_url VARCHAR not null
        )
'''
#g_on INTEGER primary key autoincrement,
try :
    cur.execute(sql)
    print('sucress')
except Exception as e:
    print(e)
    print('失败')
finally:
    cur.close()
    con.close()