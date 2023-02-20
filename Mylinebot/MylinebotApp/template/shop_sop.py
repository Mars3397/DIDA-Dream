import json
import requests

def line_liff_id(uid):
    headers = {"Authorization":"Bearer 7YLg2BzN0RDKhiJwOIrPGw2P2NmtrBGuGxoLP7d45SYkbs6wCKpvt4ORibJHpuQuZ5MYh74ENZBcB877FCtP2xHyNMjglSeaSjqrI/52XTuutL0x5myGUlx1z5is0p5pBBkJ+ty/N0Y2cJus3hVYZY9PbdgDzCFqoOLOYbqAITQ=","Content-Type":"application/json"}
    datas = {
        "view": {
            "type": "tall",
            "url": "https://2022.dida-dream.com/redirect.php?uid="+str(uid)+"&flag=rs"
        },
        "description": "shop_sop"+str(uid),
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

def shop_sop(uid):
    content = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "商家模式",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#000000"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "透過即食予，有效曝光貴公司的即期品",
                            "color": "#666666",
                            "size": "sm",
                            "flex": 1,
                            "wrap": True,
                            "margin": "none"
                        },
                        {
                            "type": "text",
                            "text": "步驟：",
                            "color": "#624669",
                            "size": "md",
                            "flex": 1,
                            "wrap": True,
                            "margin": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "1.點擊「填寫表單」按鈕",
                            "color": "#000000",
                            "size": "sm",
                            "flex": 1,
                            "wrap": True,
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": "2.客服將主動與您聯繫，討論前期建檔、後續運作流程",
                            "color": "#000000",
                            "size": "sm",
                            "flex": 1,
                            "wrap": True,
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": "3.營業期間於官網操作，更新即期品數量",
                            "color": "#000000",
                            "size": "sm",
                            "flex": 1,
                            "wrap": True,
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": "4.主動推播商品資訊給有興趣的受眾",
                            "color": "#000000",
                            "size": "sm",
                            "flex": 1,
                            "wrap": True,
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": "成為會員：",
                            "color": "#624669",
                            "size": "md",
                            "flex": 1,
                            "wrap": True,
                            "margin": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "點擊「成為會員」，獲取「加入 LINE SPOT 優惠地圖」、「搜尋引擎推播」等獨家曝光機會",
                            "color": "#000000",
                            "size": "sm",
                            "flex": 1,
                            "wrap": True,
                            "margin": "sm"
                        }
                        ]
                    }
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
                        "label": "填寫表單",
                        "uri": "https://linecorp.com"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "成為會員",
                        "uri": "https://liff.line.me/1657635549-N79kd2nl"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }


    
    #z = json.dumps(content)
    return content