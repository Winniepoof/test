import sqlite3

def process_item(item):
    con=sqlite3.connect('d:/GitHub/sqlzzj.db')
    cur=con.cursor()
    sql = 'insert into src(srcs) values(?)'

    try:
        cur.execute(sql,(item,))
        con.commit()
        print('插入成功')
    except Exception as e:
        print(e)
        con.rollback()
        print('插入失败')
    finally:
        cur.close()
        con.close()