import pymysql
import sqlite3

con=pymysql.connect(host='localhost',user='root',password='root',database='test1',port=3306)

#print(con)

cur=con.cursor()#游标对象

sql='''
    select * from t_zhang'''


try :
    cur.execute(sql)
    zhang=cur.fetchall()
    for i in zhang:
        print(i)

    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    cur.close()
    con.close()