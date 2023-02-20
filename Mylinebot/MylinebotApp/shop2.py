import pymysql
import requests
import json
s = "000053"
data = { "oldPKeys":[s], "PostInfo": "200", "Latitude": 0, "Longitude": 0, "ProjectCode":'202106302'}
r = requests.post('https://stamp.family.com.tw/api/maps/MapProductInfo', 
                        json = data )
for k in r.json()['data']:
    print(k['oldPKey'], k['name'])
def search_shop(shop_id):

    data = { "oldPKeys":[shop_id], "PostInfo": "", "Latitude": 0, "Longitude": 0, "ProjectCode":'202106302'}
    r = requests.post('https://stamp.family.com.tw/api/maps/MapProductInfo', 
                        json = data )

    ### search by shopID
    shop_info = r.json()
    shop_cur_food = []
    if len(shop_info['data'])!=0:
        food = shop_info['data'][0]['info']
        #print(shop_info)
        #print("---------------")

        shop_cur_food = []
        tag = ["飯糰手卷", "飯類主食", "麵類主食", "湯品小吃", "三明治沙拉", "蔬果", "麵包甜點", "吐司蛋糕"]
        for i in range(len(food)):
            food_of_cat =  food[i]['categories']
            for f in  food_of_cat:
                for item in f['products']:
                    shop_cur_food.append([item['code'], shop_id, food[i]['name'] , 24 , 30, item['qty']])
                    # food_id/ shop_id/ food_category/ expire_time/ price/ quantity

    return shop_cur_food
