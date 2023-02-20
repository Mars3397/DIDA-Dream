import json
import requests

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


def update_info_requester(uid):
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
                                "label": "修改偏好設定",
                                "uri": "https://liff.line.me/"+line_liff_id(uid)
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