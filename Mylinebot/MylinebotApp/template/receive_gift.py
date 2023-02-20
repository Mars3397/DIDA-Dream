def receive_gift():
    content = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://2022.dida-dream.com/src/gift5.PNG",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                "type": "uri",
                "uri": "http://linecorp.com/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://2022.dida-dream.com/src/gift-small.png",
                    "size": "xs",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                    },
                    "align": "start",
                    "position": "absolute",
                    "margin": "xxl",
                    "offsetTop": "xxl"
                },
                {
                    "type": "text",
                    "text": "[ 即食予 ] 即食卷",
                    "weight": "regular",
                    "size": "xl",
                    "align": "center",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "offsetStart": "xl",
                    "margin": "none"
                },
                {
                    "type": "text",
                    "text": "恭喜您獲得即時卷！以下為附近有即期品的商家，請於 3 天內兌換",
                    "weight": "regular",
                    "size": "sm",
                    "align": "start",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "offsetStart": "none",
                    "margin": "xxl",
                    "wrap": True
                }
                ]
            },
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
                    "label": "打開我的禮物",
                    "uri": "https://linecorp.com"
                    },
                    "color": "#000000"
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "傳送感謝小卡",
                    "uri": "https://linecorp.com"
                    },
                    "color": "#000000"
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


    
    #z = json.dumps(content)
    return content