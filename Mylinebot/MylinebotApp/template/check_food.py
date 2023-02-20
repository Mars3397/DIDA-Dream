import json
import requests
import urllib.parse

# def check_food(s_category, s_name, m_name, m_quantity):
#     content = {   "type": "carousel",
#                   "contents": [
#                         {
#                         "type": "bubble",
#                         "body": {
#                             "type": "box",
#                             "layout": "vertical",
#                             "contents": [
#                             {
#                                 "type": "text",
#                                 "text": s_category[0],
#                                 "weight": "bold",
#                                 "size": "xl"
#                             },
#                             {
#                                 "type": "box",
#                                 "layout": "baseline",
#                                 "margin": "md",
#                                 "contents": [
#                                 {
#                                     "type": "text",
#                                     "text": s_name[0],
#                                     "size": "md",
#                                     "margin": "none",
#                                     "flex": 0
#                                 }
#                                 ]
#                             },
#                             {
#                                 "type": "box",
#                                 "layout": "vertical",
#                                 "margin": "lg",
#                                 "spacing": "sm",
#                                 "contents": [
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[0],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[0],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 },
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[1],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[1],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 },
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[2],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[2],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 }
#                                 ]
#                             }
#                             ]
#                         }
#                         },
#                         {
#                         "type": "bubble",
#                         "body": {
#                             "type": "box",
#                             "layout": "vertical",
#                             "contents": [
#                             {
#                                 "type": "text",
#                                 "text": s_category[1],
#                                 "weight": "bold",
#                                 "size": "xl"
#                             },
#                             {
#                                 "type": "box",
#                                 "layout": "baseline",
#                                 "margin": "md",
#                                 "contents": [
#                                 {
#                                     "type": "text",
#                                     "text": s_name[1],
#                                     "size": "md",
#                                     "margin": "none",
#                                     "flex": 0
#                                 }
#                                 ]
#                             },
#                             {
#                                 "type": "box",
#                                 "layout": "vertical",
#                                 "margin": "lg",
#                                 "spacing": "sm",
#                                 "contents": [
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[3],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[3],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 },
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[4],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[4],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 },
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[5],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[5],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 }
#                                 ]
#                             }
#                             ]
#                         }
#                         },
#                         {
#                         "type": "bubble",
#                         "body": {
#                             "type": "box",
#                             "layout": "vertical",
#                             "contents": [
#                             {
#                                 "type": "text",
#                                 "text": s_category[2],
#                                 "weight": "bold",
#                                 "size": "xl"
#                             },
#                             {
#                                 "type": "box",
#                                 "layout": "baseline",
#                                 "margin": "md",
#                                 "contents": [
#                                 {
#                                     "type": "text",
#                                     "text": s_name[2],
#                                     "size": "md",
#                                     "margin": "none",
#                                     "flex": 0
#                                 }
#                                 ]
#                             },
#                             {
#                                 "type": "box",
#                                 "layout": "vertical",
#                                 "margin": "lg",
#                                 "spacing": "sm",
#                                 "contents": [
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[6],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[6],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 },
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[7],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[7],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 },
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": m_name[8],
#                                         "size": "sm",
#                                         "flex": 5
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": m_quantity[8],
#                                         "wrap": True,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 1
#                                     }
#                                     ]
#                                 }
#                                 ]
#                             }
#                             ]
#                         }
#                         },
#                         {
#                         "type": "bubble",
#                         "body": {
#                             "type": "box",
#                             "layout": "vertical",
#                             "contents": [
#                             {
#                                 "type": "button",
#                                 "action": {
#                                 "type": "uri",
#                                 "label": "查看更多",
#                                 "uri": "https://liff.line.me/1657635549-PbvBj8ao"
#                                 }
#                             }
#                             ]
#                         }
#                         }
#                   ]
#                 }


    
#     #z = json.dumps(content)
#     return content

def line_liff_id(uid):
    headers = {"Authorization":"Bearer 7YLg2BzN0RDKhiJwOIrPGw2P2NmtrBGuGxoLP7d45SYkbs6wCKpvt4ORibJHpuQuZ5MYh74ENZBcB877FCtP2xHyNMjglSeaSjqrI/52XTuutL0x5myGUlx1z5is0p5pBBkJ+ty/N0Y2cJus3hVYZY9PbdgDzCFqoOLOYbqAITQ=","Content-Type":"application/json"}
    datas = {
        "view": {
            "type": "tall",
            "url": "https://2022.dida-dream.com/redirect.php?uid="+str(uid)+"&flag=eu"
        },
        "description": "update_info"+str(uid),
        "features": {
            "ble": True,
            "qrCode": True
        },
        "permanentLinkPattern": "concat",
        "scope": ["profile", "chat_message.write"],
        "botPrompt": "none"
    }
    req = requests.request('POST', 'https://api.line.me/liff/v1/apps', headers=headers, data=json.dumps(datas).encode('utf-8'))
    x = req.text.split("\"")
    return x[3]

def check_food(s_category, s_name, shop_star, shop_level, m_number, m_name, m_quantity):
    shops = []
    k = 0
    for i in range(len(s_category)):
        if i == 5:
            break
        meals_content = []
        for j in range(m_number[i]):
            meal = {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": m_name[k],#m_name[3]
                            "size": "sm",
                            "flex": 5
                        },
                        {
                            "type": "text",
                            "text": f'{m_quantity[k]}',#m_quantity[3]
                            "wrap": True,
                            "color": "#666666",
                            "size": "sm",
                            "flex": 1
                        }
                        ]
                    }
            meals_content.append(meal)
            k = k + 1
        shop_category = {
                            "type": "text",
                            "text": s_category[i], 
                            "weight": "bold",
                            "align": "center",
                            "size": "xl"
                        }
        
        shop_name = {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "text",
                            "text": s_name[i],
                            "size": "md",
                            "margin": "none",
                            "flex": 0
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            "offsetStart": "md"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            "offsetStart": "md"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            "offsetStart": "md"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            "offsetStart": "md"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            "offsetStart": "md"
                        },
                        {
                            "type": "text",
                            "text": shop_star[i],
                            "offsetStart": "lg"
                        }
                        ]
                    }
        
        meals = {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": meals_content
                }
        
        image = {
                    "type": "image",
                    "url": "https://2022.dida-dream.com/src/mem_b.PNG",
                    "size": "xxs",
                    "aspectRatio": "13:13",
                    "aspectMode": "cover",
                    "position": "absolute",
                    "offsetEnd": "md",
                    "offsetTop": "xxl"
                }
        print("haha2")
        if shop_level[i] == '1':
            image = {
                    "type": "image",
                    "url": "https://2022.dida-dream.com/src/mem.PNG",
                    "size": "xxs",
                    "aspectRatio": "13:13",
                    "aspectMode": "cover",
                    "position": "absolute",
                    "offsetEnd": "md",
                    "offsetTop": "xxl"
                }
        elif shop_level[i] == '2':
            image = {
                    "type": "image",
                    "url": "https://2022.dida-dream.com/src/mem_b.PNG",
                    "size": "xxs",
                    "aspectRatio": "13:13",
                    "aspectMode": "cover",
                    "position": "absolute",
                    "offsetEnd": "md",
                    "offsetTop": "xxl"
                }
        elif shop_level[i] == '3':
            image = {
                    "type": "image",
                    "url": "https://2022.dida-dream.com/src/mem_s.PNG",
                    "size": "xxs",
                    "aspectRatio": "13:13",
                    "aspectMode": "cover",
                    "position": "absolute",
                    "offsetEnd": "md",
                    "offsetTop": "xxl"
                }
        elif shop_level[i] == '4':
            image = {
                    "type": "image",
                    "url": "https://2022.dida-dream.com/src/mem_g.PNG",
                    "size": "xxs",
                    "aspectRatio": "13:13",
                    "aspectMode": "cover",
                    "position": "absolute",
                    "offsetEnd": "md",
                    "offsetTop": "xxl"
                }
        url = s_category[i]
        url = "https://spot.line.me/search/location?q=" + urllib.parse.quote(url)
        sub_shop = {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            shop_category, image, shop_name, meals
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "商家資訊",
                            "uri": url
                            }
                        }
                        ],
                        "flex": 0
                    }
                    }
        shops.append(sub_shop)
        print("haha")
    print("here")
    more = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "https://liff.line.me/1657635549-OWpaWBKL"
                    }
                }
                ]
            }
            }
    shops.append(more)
    content = {   "type": "carousel",
                    "contents": shops
            }
    print(content)
    return content

