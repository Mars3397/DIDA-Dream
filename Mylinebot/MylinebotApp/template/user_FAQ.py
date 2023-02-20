import json
import requests

def user_FAQ():
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
                "text": "【 成立宗旨 】",
                "weight": "bold",
                "size": "md"
                },
                {
                "type": "text",
                "text": "「打造一個即期品整合平台，把剩食送到需要的人手中。」 透過即食予官方帳號，您可以即時取得即期品優惠資訊，也能透過即食予捐贈計畫，贈送即食卷給需要幫助的人",
                "size": "xs",
                "wrap": True,
                "margin": "lg"
                },
                {
                "type": "text",
                "text": "【 常見問題 】",
                "weight": "bold",
                "size": "md",
                "margin": "xxl"
                },
                {
                "type": "text",
                "text": "待補",
                "size": "xs",
                "wrap": True,
                "margin": "lg"
                },
                {
                "type": "text",
                "text": "【 功能說明 - 主選單 】",
                "weight": "bold",
                "size": "md",
                "margin": "xxl"
                },
                {
                "type": "text",
                "text": "- 查詢即期品：搜尋特定即期品",
                "size": "xs",
                "wrap": True,
                "margin": "lg"
                },
                {
                "type": "text",
                "text": "- 優惠地圖：查看附近店家即期品庫存",
                "size": "xs",
                "wrap": True,
                "margin": "md"
                },
                {
                "type": "text",
                "text": "- 資料修改：修改個人偏好",
                "size": "xs",
                "wrap": True,
                "margin": "md"
                },
                {
                "type": "text",
                "text": "- 推薦給好友：分享此官方帳號給 LINE 好友",
                "size": "xs",
                "wrap": True,
                "margin": "md"
                },
                {
                "type": "text",
                "text": "- 聯絡我們：常見問題 & 真人客服聯繫",
                "size": "xs",
                "wrap": True,
                "margin": "md"
                },
                {
                "type": "text",
                "text": "【 功能說明 - 即食予 】",
                "weight": "bold",
                "size": "md",
                "margin": "xxl"
                },
                {
                "type": "text",
                "text": "- 發送即食卷：捐贈即食券給有需要的人",
                "size": "xs",
                "wrap": True,
                "margin": "lg"
                },
                {
                "type": "text",
                "text": "- 集點卡：查看集點進度",
                "size": "xs",
                "wrap": True,
                "margin": "md"
                },
                {
                "type": "text",
                "text": "- 了解計畫：計畫運作細節、常見問題",
                "size": "xs",
                "wrap": True,
                "margin": "md"
                },
                {
                "type": "text",
                "text": "- 支持我們：捐贈計畫營運資金，並集點",
                "size": "xs",
                "wrap": True,
                "margin": "md"
                }
                ]
                }
                }
                ]
                }


    
    #z = json.dumps(content)
    return content