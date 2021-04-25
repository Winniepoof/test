
import sqlite3

con=sqlite3.connect('d:/GitHub/testspider.db')

print(con)

cur=con.cursor()#游标对象

sql='''create table url(
        pon INTEGER primary key autoincrement,
        pdata VARCHAR not null
        )
'''
try :
    cur.execute(sql)
    print('sucress')
except Exception as e:
    print(e)
    print('失败')
finally:
    cur.close()
    con.close()
