import json
import requests

def check_food_title():
    content = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5,
                        "text": "你知道嗎？只要送出一張即食券，就能照亮一個家庭 ✨ 點擊選單的「即食予」，為剩食再分配盡一份力 🙌",
                        "margin": "none",
                        "offsetTop": "none",
                        "offsetBottom": "none",
                        "offsetStart": "none",
                        "offsetEnd": "none",
                        "weight": "regular",
                        "style": "normal"
                    }
                    ]
                }
                }
    return content