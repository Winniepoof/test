
import sqlite3

con=sqlite3.connect('d:/GitHub/test1.db')


cur=con.cursor()
#游标对象

sql='delete from t_person  where pon=?'

try :
    cur.execute(sql,(2,))
    con.commit()
    print('删除成功')

except Exception as e:
    print(e)
    con.rollback()
    print('查询失败')
finally:
    cur.close()
    con.close()