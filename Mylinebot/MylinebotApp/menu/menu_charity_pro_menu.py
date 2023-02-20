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
          "action": {"type": "message", "text": "Charity Pro Menu"}
        },
        {
          "bounds": {"x": 400, "y": 0, "width": 400, "height": 93},
          "action": {"type": "message", "text": "Charity Pro Request"}
        },
        {
          "bounds": {"x": 800, "y": 0, "width": 400, "height": 93},
          "action": {"type": "uri",
                      "label": "MY DIDA",
                      "uri": 'https://liff.line.me/1657635549-Gllkgw3o'}
        },
        {
          "bounds": {"x": 0, "y": 93, "width": 300, "height": 358},
          "action": {"type": "message", "text": "查詢即期品"}
        },
        {
          "bounds": {"x": 300, "y": 93, "width": 300, "height": 358},
          "action": {"type": "message", "text": "資料修改"}
        },
        {
          "bounds": {"x": 600, "y": 93, "width": 300, "height": 358},
          "action": {"type": "message", "text": "優惠地圖"}
        },
        {
          "bounds": {"x": 900, "y": 93, "width": 300, "height": 358},
          "action": {"type": "message", "text": "禮卷購買"}
        },
        {
          "bounds": {"x": 0, "y": 451, "width": 300, "height": 358},
          "action": {"type": "message", "text": "即食予"}
        },
        {
          "bounds": {"x": 300, "y": 451, "width": 300, "height": 358},
          "action": {"type": "uri",
                      "label": "MY DIDA",
                      "uri": 'https://liff.line.me/1657635549-p87K6gk3'}
        },
        {
          "bounds": {"x": 600, "y": 451, "width": 300, "height": 358},
          "action": {"type": "message", "text": "FAQ"}
        },
        {
          "bounds": {"x": 900, "y": 451, "width": 300, "height": 358},
          "action": {"type": "message", "text": "折扣預約"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text) #richmenu-999c34889be427db0df31c1e31b3fda6

x = req.text.split("\"")


with open("image/charity_pro_menu.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(x[3], "image/jpeg", f)

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+x[3], 
                       headers=headers)


