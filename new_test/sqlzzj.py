import pymysql
import sqlite3


def savesql(product):
    con=sqlite3.connect('d:/GitHub/sqlzzj.db')
    #print(con)
    cur=con.cursor()#游标对象
    sql='insert into src(url) values(?)'

    try :
        #cur.executemany(sql,[(product[0],product[1],product[2],product[3],)])
        cur.execute(sql,('张三'))
        con.commit()
        print('插入成功')
    except Exception as e:
        print(e)
        con.rollback()
        print('插入失败')
    finally:
        cur.close()
        con.close()