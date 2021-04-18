
import sqlite3

con=sqlite3.connect('d:/Pycharmprojects/test.db')

print(con)

cur=con.cursor()#游标对象

sql='insert into t_person(pname,age) values(?,?)'

try :
    cur.executemany(sql,[('zxl',21),('lxn',21),('张淼鑫',21)])
    #cur.execute(sql,('张三',24))
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    cur.close()
    con.close()