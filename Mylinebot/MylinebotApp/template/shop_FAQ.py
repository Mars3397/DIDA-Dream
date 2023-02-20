import json
import requests

def shop_FAQ():
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
                            "text": "【 功能說明 - 商家主選單 】",
                            "weight": "bold",
                            "size": "md",
                            "margin": "xxl"
                        },
                        {
                            "type": "text",
                            "text": "- 商品修改：新增＆更新即期品資訊",
                            "size": "xs",
                            "wrap": True,
                            "margin": "lg"
                        },
                        {
                            "type": "text",
                            "text": "- 加入會員：了解會員功能與權益",
                            "size": "xs",
                            "wrap": True,
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "- 刊登優惠：上傳優惠到 LINE SPOT",
                            "size": "xs",
                            "wrap": True,
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "- 資料修改：修改店家基本資訊",
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
                            "text": "【 功能說明 - 其他功能 】",
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
                            "text": "- 推薦給好友：分享此官方帳號給 LINE 好友",
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
                            "text": "- 參與計畫：捐贈即期品，並獲得榮譽徽章",
                            "size": "xs",
                            "wrap": True,
                            "margin": "lg"
                        },
                        {
                            "type": "text",
                            "text": "- 了解計畫：回饋、運作細節、常見問題",
                            "size": "xs",
                            "wrap": True,
                            "margin": "lg"
                        }
                        ]
                    }
                    }
                ]
                }


    
    #z = json.dumps(content)
    return content