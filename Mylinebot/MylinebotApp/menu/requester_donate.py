import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)

headers = {"Authorization":"Bearer VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
line_bot_api = LineBotApi('VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU=')
# liff_api = LIFF('VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU=')

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
                      "richMenuAliasId": "requester_menu",
                      "data": "richmenu=requester_menu"
                    }
        },
        {
          "bounds": {"x": 600, "y": 0, "width": 600, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "requester_donate",
                      "data": "richmenu=requester_donate"
                    }
        },
        {
          "bounds": {"x": 175, "y": 660, "width": 850, "height": 100},
          "action": {"type": "message", "text": "了解計畫"}
        },
        {
          "bounds": {"x": 0, "y": 93, "width": 1200, "height": 717},
          "action": {"type": "message", "text": "收取即食卷"}
        }
        
    ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text) # richmenu-7e7996c1857bb4ff40fa7c9f1da89f10

x = req.text.split("\"")


with open("image/requester_donate.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(x[3], "image/png", f)

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+x[3], 
                       headers=headers)


