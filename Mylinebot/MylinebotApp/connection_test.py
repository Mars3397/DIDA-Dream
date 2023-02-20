import pymysql


connect_db = pymysql.connect(user='DIDA-Dream', password='didadida15w', host='68.178.145.107',port=3306, database='DIDA-Dream')
print(connect_db)