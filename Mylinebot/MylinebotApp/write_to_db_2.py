import shop
import shop2
import pymysql
#import shop_id
import shop_data
import time

connect_db = pymysql.connect(host = 'localhost', user='DIDA-Dream', passwd='didadida15w', charset='utf8mb4', db='mysql')
localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
print(result)
#connect_db = pymysql.connect(host = 'localhost', user='root', passwd='', charset='utf8', db='familymart') #didadida15w
count = 0
with connect_db.cursor() as cursor:
    print("start_storing_food")
    sql_food_id = """
    CREATE TABLE IF NOT EXISTS food_id(
        m_id varchar(10) not null,
        m_name varchar(50) not null
    );
    """
    sql_meals = """
    CREATE TABLE IF NOT EXISTS meals(
        m_id varchar(10) not null,
        s_id varchar(10) not null,
        m_group varchar(256) not null,
        m_time varchar(10) not null,
        m_price int unsigned not null,
        m_quantity int unsigned not null
    );
    """
    #psql='''\copy food FROM 'D:/line_fresh/shop2/csv_food.csv' DELIMITER ',' CSV header'''
    #cursor.execute(sql_food_id)
    #cursor.execute(sql_meals)
    # cursor.execute("TRUNCATE TABLE MylinebotApp_food_id")
    # cursor.execute("TRUNCATE TABLE MylinebotApp_meals")
    food_id = shop.get_food_id_list() 
    #print(food_id)
    # 先用product ID找到meal name, meals只放name不放id 
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
    #print(result)
    all_family_food = []
    count = 0
    for shop_id in shop_data.all_shop_id[3000:4000]:
        shop_food = shop2.search_shop(shop_id)
        for d in shop_food:
            #count+=1
            name = food_id[d[0]]
            update = """
            insert into MylinebotApp_meals(m_name,s_id,m_group,m_price,m_quantity)
            
            values('%s','%s','%s',%s,%s)""" % (name,d[1],d[2],d[4],d[5])
            print((name,d[1],d[2],d[3],d[4],d[5]))
            #count = count + 1
            # print(count)
            cursor.execute(update)
        count += 1
        print(count)
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
    #print(result)
    #print(count)
    connect_db.commit()
    
connect_db.close()
print("stop_storing_food")


#print(all_family_food)