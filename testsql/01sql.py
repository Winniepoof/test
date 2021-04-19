
import sqlite3

con=sqlite3.connect('d:/GitHub/test1.db')

print(con)

cur=con.cursor()#游标对象

sql='''create table t_person(
        pon INTEGER primary key autoincrement,
        pname VARCHAR not null,
        age INTEGER
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
