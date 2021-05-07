import pymysql
import sqlite3


def savesql(product):
    con=sqlite3.connect('d:/GitHub/tspider.db')
    #print(con)
    cur=con.cursor()#游标对象
    sql='insert into good(g_title,g_price,g_shop) values(?,?,?)'

    try :
        cur.executemany(sql,[(product[0],product[1],product[2],)])
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