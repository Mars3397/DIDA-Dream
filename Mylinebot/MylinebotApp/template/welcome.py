import json
import requests

def welcome(uid):
    content = {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://2022.dida-dream.com/linebot/welcome.PNG",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "歡迎加入即食予計畫",
                            "weight": "bold",
                            "size": "xl"
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
                            "label": "一般使用者註冊",
                            "uri": "https://liff.line.me/1657635549-J0klqVGR"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "商家註冊",
                            "uri": "https://liff.line.me/1657635549-N79kd2nl"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "了解即食予計畫",
                            "text": "了解計畫"
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
                ]
                }


    
    #z = json.dumps(content)
    return content