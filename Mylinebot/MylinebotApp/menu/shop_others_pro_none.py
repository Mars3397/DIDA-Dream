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
          "bounds": {"x": 0, "y": 93, "width": 800, "height": 710},
          "action": {"type": "uri",
                      "label": "check food",
                      "uri": 'https://liff.line.me/1657635549-OWpaWBKL'} # 查詢即期品
        },
        {
          "bounds": {"x": 800, "y": 93, "width": 400, "height": 355},
          "action": {"type": "uri",
                      "label": "line spot",
                      "uri": 'https://liff.line.me/1657635549-y0KwqmZb'} # 優惠地圖
        },
        {
          "bounds": {"x": 800, "y": 448, "width": 400, "height": 355},
          "action": {"type": "uri",
                      "label": "line spot",
                      "uri": 'https://liff.line.me/1657635549-35pzekgQ'} # 推薦給好友
        }
        
    ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text) # richmenu-6719042a802926b6cfe5df852d84ae92

x = req.text.split("\"")


with open("image/shop_others.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(x[3], "image/png", f)

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+x[3], 
                       headers=headers)


