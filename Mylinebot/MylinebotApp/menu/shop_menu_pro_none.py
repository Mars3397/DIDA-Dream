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
          "bounds": {"x": 0, "y": 0, "width": 400, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "shop_menu_pro_none",
                      "data": "richmenu=shop_menu_pro_none"
                    }
        },
        {
          "bounds": {"x": 400, "y": 0, "width": 400, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "shop_others_pro_none",
                      "data": "richmenu=shop_others_pro_none"
                    }
        },
        {
          "bounds": {"x": 800, "y": 0, "width": 400, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "shop_donate_pro_none",
                      "data": "richmenu=shop_donate_pro_none"
                    }
        },
        {
          "bounds": {"x": 0, "y": 93, "width": 730, "height": 760},
          "action": {"type": "uri",
                      "label": "shop",
                      "uri": 'https://liff.line.me/1657635549-3Qg9zW6M'} # 商品修改
        },
        {
          "bounds": {"x": 730, "y": 93, "width": 470, "height": 410},
          "action": {"type": "message", "text": "加入會員"}
        },
        {
          "bounds": {"x": 730, "y": 503, "width": 235, "height": 300}, # https://liff.line.me/1657635549-yM4MZE73
          "action": {"type": "uri",
                      "label": "edit user",
                      "uri": 'https://liff.line.me/1657635549-yM4MZE73'} # 資料修改
        },
        {
          "bounds": {"x": 965, "y": 503, "width": 235, "height": 300},
          "action": {"type": "message", "text": "聯絡我們"}
        }
        
    ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text) # richmenu-8e32ccac93db2b7ededd6f7ccdb094fb

x = req.text.split("\"")


with open("image/shop_menu.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(x[3], "image/png", f)

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+x[3], 
                       headers=headers)


