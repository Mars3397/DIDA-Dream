import json
import requests

def test():
    content = {   "type": "carousel",
                  "contents": [
                        {
                        "type": "bubble",
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
                                "label": "測試測試",
                                "uri": "https://liff.line.me/1657635549-yM4MZE73"
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