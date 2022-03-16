import pymysql

con=pymysql.connect(host='localhost',user='root',password='root',database='zzj',port=3306)
#print(con)

cur=con.cursor()

sql='''create table src(
    zno int primary key auto_increment,
    src varchar(30) not null
    )
    '''

try :
    cur.execute(sql)
    #con.commit()
    print('创建成功')

except Exception as e:
    print(e)
    #con.rollback()
    print('查询失败')
finally:
    cur.close()
    con.close()