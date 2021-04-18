
import sqlite3

con=sqlite3.connect('d:/Pycharmprojects/test.db')

print(con)

cur=con.cursor()#游标对象

sql='select *from t_person'

try :
    cur.execute(sql)
    person_all=cur.fetchall()
    #print(person_all)
    for i in person_all:
        print(i)
except Exception as e:
    print(e)
    con.rollback()
    print('查询失败')
finally:
    cur.close()
    con.close()