
import sqlite3

con=sqlite3.connect('d:/GitHub/test.db')

print(con)

cur=con.cursor()#游标对象

sql='select *from t_person'

try :
    cur.execute(sql)
    person=cur.fetchone()
    print(person)
    # for i in person:
    #     print(i)
except Exception as e:
    print(e)
    con.rollback()
    print('查询失败')
finally:
    cur.close()
    con.close()