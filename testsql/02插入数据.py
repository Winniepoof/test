
import sqlite3

con=sqlite3.connect('d:/GitHub/test1.db')

print(con)

cur=con.cursor()#游标对象

sql='insert into t_person(pname,age) values(?,?)'

try :
    cur.executemany(sql,[('张起灵',21),('张启山',21),('张海琪',21)])
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