import json
import requests

def support_us():
    content = {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "【 支持我們 】",
                            "weight": "bold",
                            "size": "md",
                            "margin": "xxl"
                        },
                        {
                            "type": "text",
                            "text": "認同我們理念嗎？想為這個計畫貢獻更多嗎？我們將開放個人捐款管道，讓大家可以為計畫捐贈營運資金！",
                            "size": "xs",
                            "wrap": True,
                            "margin": "lg"
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "（本功能與 LINE PAY 洽談中 ... ）",
                                "size": "sm",
                                "margin": "none"
                            }
                            ]
                        }
                        ]
                    }
                    }
                ]
                }


    
    #z = json.dumps(content)
    return content