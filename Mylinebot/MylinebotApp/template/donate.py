import json
def donate():
    content = {   "type": "carousel",
                  "contents": [
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://2022.dida-dream.com/linebot/f1.PNG",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
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
                                "label": "捐贈",
                                "uri": "https://liff.line.me/1657635549-90Vya6L5"
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
                        },
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://2022.dida-dream.com/linebot/f2.PNG",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "action": {
                            "type": "uri",
                            "uri": "http://linecorp.com/"
                            }
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
                                "label": "捐贈",
                                "uri": "https://liff.line.me/1657635549-90Vya6L5"
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
                        },
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://2022.dida-dream.com/linebot/f3.PNG",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
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
                                "type": "postback",
                                "label": "捐贈",
                                "data": "捐贈"
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
                        },
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://2022.dida-dream.com/linebot/f4.PNG",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
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
                                "type": "postback",
                                "label": "捐贈",
                                "data": "捐贈"
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
                        },
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://2022.dida-dream.com/linebot/f5.PNG",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
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
                                "type": "postback",
                                "label": "捐贈",
                                "data": "捐贈"
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