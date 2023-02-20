import json
import family_shop
print(family_shop.family_table)


# def check_food(s_category, s_name, m_number, m_name, m_quantity):
    
#     # content = {   "type": "carousel",
#     #               "contents": [
                        
#     #                     {
#     #                     "type": "bubble",
#     #                     "body": {
#     #                         "type": "box",
#     #                         "layout": "vertical",
#     #                         "contents": [
#     #                         {
#     #                             "type": "text",
#     #                             "text": "s_category[1]", #s_category
#     #                             "weight": "bold",
#     #                             "size": "xl"
#     #                         },
#     #                         {
#     #                             "type": "box",
#     #                             "layout": "baseline",
#     #                             "margin": "md",
#     #                             "contents": [
#     #                             {
#     #                                 "type": "text",
#     #                                 "text": "s_name[1]", #s_name[1]
#     #                                 "size": "md",
#     #                                 "margin": "none",
#     #                                 "flex": 0
#     #                             }
#     #                             ]
#     #                         },
#     #                         {
#     #                             "type": "box",
#     #                             "layout": "vertical",
#     #                             "margin": "lg",
#     #                             "spacing": "sm",
#     #                             "contents": [
#     #                             {
#     #                                 "type": "box",
#     #                                 "layout": "baseline",
#     #                                 "spacing": "sm",
#     #                                 "contents": [
#     #                                 {
#     #                                     "type": "text",
#     #                                     "text": "m_name[3]",#m_name[3]
#     #                                     "size": "sm",
#     #                                     "flex": 5
#     #                                 },
#     #                                 {
#     #                                     "type": "text",
#     #                                     "text": "m_quantity[3]",#m_quantity[3]
#     #                                     "wrap": True,
#     #                                     "color": "#666666",
#     #                                     "size": "sm",
#     #                                     "flex": 1
#     #                                 }
#     #                                 ]
#     #                             }
#     #                             ]
#     #                         }
#     #                         ]
#     #                     }
#     #                     },
#     #                     {
#     #                     "type": "bubble",
#     #                     "body": {
#     #                         "type": "box",
#     #                         "layout": "vertical",
#     #                         "contents": [
#     #                         {
#     #                             "type": "button",
#     #                             "action": {
#     #                             "type": "uri",
#     #                             "label": "查看更多",
#     #                             "uri": "https://liff.line.me/1657635549-PbvBj8ao"
#     #                             }
#     #                         }
#     #                         ]
#     #                     }
#     #                     }
#     #               ]
#     #             }
    
    
    
#     shops = []
#     k = 0
#     for i in range(len(s_category)):
#         meals_content = []
#         for j in range(m_number[i]):
#             meal = {
#                         "type": "box",
#                         "layout": "baseline",
#                         "spacing": "sm",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": m_name[k],#m_name[3]
#                             "size": "sm",
#                             "flex": 5
#                         },
#                         {
#                             "type": "text",
#                             "text": f'{m_quantity[k]}',#m_quantity[3]
#                             "wrap": True,
#                             "color": "#666666",
#                             "size": "sm",
#                             "flex": 1
#                         }
#                         ]
#                     }
#             meals_content.append(meal)
#             k = k + 1
#         shop_category = {
#                             "type": "text",
#                             "text": s_category[i], 
#                             "weight": "bold",
#                             "align": "center",
#                             "size": "xl"
#                         }
#         shop_name = {
#                         "type": "box",
#                         "layout": "baseline",
#                         "margin": "md",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": s_name[i],
#                             "size": "md",
#                             "margin": "none",
#                             "flex": 0
#                         },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
#                 "offsetStart": "md"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
#                 "offsetStart": "md"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
#                 "offsetStart": "md"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
#                 "offsetStart": "md"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
#                 "offsetStart": "md"
#               },
#               {
#                 "type": "text",
#                 "text": "5.0",
#                 "offsetStart": "lg"
#               }
#                         ]
#                     }
#         meals = {
#                     "type": "box",
#                     "layout": "vertical",
#                     "margin": "lg",
#                     "spacing": "sm",
#                     "contents": meals_content
#                 }
#         image = {
#                     "type": "image",
#                     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
#                     "size": "xxs",
#                     "aspectRatio": "20:13",
#                     "aspectMode": "cover",
#                     "action": {
#                     "type": "uri",
#                     "uri": "http://linecorp.com/"
#                     },
#                     "position": "absolute",
#                     "offsetEnd": "md"
#                 }
#         sub_shop = {
#                     "type": "bubble",
#                     "body": {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             shop_category, image, shop_name, meals
#                         ]
#                     },
#                     "footer": {
#                         "type": "box",
#                         "layout": "vertical",
#                         "spacing": "sm",
#                         "contents": [
#                         {
#                             "type": "button",
#                             "style": "link",
#                             "height": "sm",
#                             "action": {
#                             "type": "uri",
#                             "label": "商家資訊",
#                             "uri": "https://linecorp.com"
#                             }
#                         }
#                         ],
#                         "flex": 0
#                     }
#                     }
#         shops.append(sub_shop)
#     more = {
#             "type": "bubble",
#             "body": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                 {
#                     "type": "button",
#                     "action": {
#                     "type": "uri",
#                     "label": "查看更多",
#                     "uri": "https://liff.line.me/1657635549-PbvBj8ao"
#                     }
#                 }
#                 ]
#             }
#             }
#     shops.append(more)
#     content = {   "type": "carousel",
#                     "contents": shops
#             }
        
#     return content

# s_category = ['全家基隆精一店', '全家基隆廟口店', '全家基隆仁四店', '全家基隆新站前店', '全家基隆仁愛店']
# s_name = ['全家', '全家', '全家', '全家', '全家']
# m_number = [3, 3, 3, 3, 3]
# m_name = ['肉鬆飯糰', '鹽蔥燒肉飯糰', '雞肉飯飯糰', '經典總匯三明治', '綜合水果繽紛杯', '海鹽焦糖泡芙蛋糕', '一配鮑菇脆筍飯糰', '鮭魚鮭魚卵飯糰', '鹽蔥燒肉飯糰', '烤雞蛋蛋雙手卷', '鹽水意麵', '沙茶豬肉炒麵', '大口義式香草烤雞飯糰', '四川風味麻婆豆腐燴飯', '蕃茄肉醬義大利麵']
# m_quantity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # s_category = ['全家基隆精一店']
# # s_name = ['全家']
# # m_number = [3]
# # m_name = ['肉鬆飯糰', '鹽蔥燒肉飯糰', '雞肉飯飯糰']
# # m_quantity = [1, 1, 1]
# ans = check_food(s_category, s_name, m_number, m_name, m_quantity)
# print(json.dumps(ans))