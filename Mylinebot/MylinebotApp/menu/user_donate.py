import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)

headers = {"Authorization":"Bearer 'token'","Content-Type":"application/json"}
line_bot_api = LineBotApi('token')

# #新增LIFF頁面到LINEBOT中
# liff_id = liff_api.add(view_type="tall",view_url="https://www.youtube.com/")

body = {
    "size": {"width": 1200, "height": 810},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 600, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "user_menu",
                      "data": "richmenu=user_menu"
                    }
        },
        {
          "bounds": {"x": 600, "y": 0, "width": 600, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "user_donate",
                      "data": "richmenu=user_donate"
                    }
        },
        {
          "bounds": {"x": 0, "y": 93, "width": 730, "height": 760},
          "action": {"type": "message", "text": "發送即食卷"}
        },
        {
          "bounds": {"x": 730, "y": 93, "width": 470, "height": 410},
          "action": {"type": "uri",
                      "label": "record",
                      "uri": 'https://liff.line.me/1657635549-p87K6gk3'} # 集點卡
        },
        {
          "bounds": {"x": 730, "y": 503, "width": 235, "height": 300},
          "action": {"type": "message", "text": "支持我們"}
        },
        {
          "bounds": {"x": 965, "y": 503, "width": 235, "height": 300},
          "action": {"type": "message", "text": "了解計畫"}
        }
        
    ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text) # richmenu-f193df06c74f6daa3bf0046a7038e021

x = req.text.split("\"")


with open("image/user_donate.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(x[3], "image/png", f)

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+x[3], 
                       headers=headers)


