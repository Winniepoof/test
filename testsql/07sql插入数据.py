import pymysql
import sqlite3

con=pymysql.connect(host='localhost',user='root',password='root',database='test1',port=3306)

#print(con)

cur=con.cursor()#游标对象

sql='insert into t_zhang(name,age) values(%s,%s)'

try :
    cur.executemany(sql,[('张起灵',221),('张小鱼',121),('张启山',91)])
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