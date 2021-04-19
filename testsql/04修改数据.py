
import sqlite3

con=sqlite3.connect('d:/GitHub/test1.db')


cur=con.cursor()
#游标对象

sql='update t_person set pname=? where pon=?'

try :
    cur.execute(sql,('张金水',4))
    con.commit()

except Exception as e:
    print(e)
    con.rollback()
    print('查询失败')
finally:
    cur.close()
    con.close()