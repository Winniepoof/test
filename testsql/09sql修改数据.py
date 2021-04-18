import pymysql
import sqlite3

con=pymysql.connect(host='localhost',user='root',password='root',database='test1',port=3306)

#print(con)

cur=con.cursor()#游标对象

sql='update t_zhang set name =%s and age=%s where zno=%s'

try :
    cur.execute(sql,('zrs',20,2))
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    cur.close()
    con.close()