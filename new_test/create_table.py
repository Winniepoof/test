import sqlite3

con=sqlite3.connect('d:/GitHub/sqlzzj.db')
#print(con)
cur=con.cursor()#游标对象

sql='''create table src(  
        g_on INTEGER primary key autoincrement,     
        srcs VARCHAR not null
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