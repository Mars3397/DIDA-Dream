import json
import requests

def already_donated():
    content = {   "type": "carousel",
                  "contents": [
                        {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://2022.dida-dream.com/linebot/thankyou.PNG",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "action": {
                        "type": "uri",
                        "uri": "http://linecorp.com/"
                        }
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "感謝您的捐贈",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "一人已在台北市內湖區收到您的即食卷",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                }
                                ]
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
                            "label": "查看我的集點卡",
                            "uri": "https://liff.line.me/1657635549-4kzeQ0dV"
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