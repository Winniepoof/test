import pymysql
import tsqlite

class ScrapyspiderPipeline:
    def process_item(self, item, spider):
        db=pymysql.connect(host='localhost',user='root',password='root',db='test',charset='utf-8')
        cursor=db.cursor()

        name = item['name'][0]
        coupon_price = item['coupon_price'][0]
        old_price = item['old_price'][0]
        seller = item['seller'][0]
        sell_num = item['sell_num'][0]
        img = item['img'][0]

#(%s,%s,%s,%s,%s,%s)
        sql='INSERT INTO py(clothes_name,coupon_price,old_price,seller,sell_num,img) VALUES(?,?,?,?,?,?)'
        cursor.execute(
            sql,[(name,coupon_price,old_price,seller,sell_num,img)]
        )
        db.commit()

        cursor.close()
        db.close()
        return item