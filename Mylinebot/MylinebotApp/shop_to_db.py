# update database

from shop_id import shop_id_all
import pymysql
import time


localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
print("haha")
print(result)
#connect_db = pymysql.connect(user='root', password='didadida15w', host='68.178.145.107',port=3306, database='DIDA-Dream')
#connect_db = mysql.connector.connect(user='DIDA-Dream', password='didadida15w', host='68.178.145.107',port=3306, database='DIDA-Dream', auth_plugin='mysql_native_password')
#print(connect_db)
connect_db = pymysql.connect(host = 'localhost', user='DIDA-Dream', passwd='didadida15w', charset='utf8mb4', db='mysql')
with connect_db.cursor() as cursor:

    cursor.execute("TRUNCATE TABLE MylinebotApp_shops")
    #cursor.execute("TRUNCATE TABLE MylinebotApp_family_shops")
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
    print(result)
    for d in shop_id_all: #oldPKey, name,"全家", latitude, longitude
        update = """
        insert into MylinebotApp_shops(s_name,u_id,s_category,s_latitude,s_longtitude,s_city,s_address)
        values('%s','%s','%s',%s,%s,'%s','%s')""" % (d[1],'-1',d[2],d[3],d[4],d[5], d[6])
        update_f = """
        insert into MylinebotApp_family_shops(s_id,s_name)
        values('%s','%s')""" % (d[0],d[1])
        cursor.execute(update)
        # cursor.execute(update_f)
    connect_db.commit()
connect_db.close()
localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
print(result)
print("haha")
