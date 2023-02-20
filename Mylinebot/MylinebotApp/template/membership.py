def membership():
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
                            "text": "【 Dida Membership 】",
                            "weight": "bold",
                            "size": "md",
                            "margin": "xxl"
                        },
                        {
                            "type": "text",
                            "text": "Dida Membership 是我們專為商家設計的會員制度，總共分為三個等級，  我們會將部分會費作為購買即食券的費用，讓商家在享有會員回饋的同時，提升企業形象。",
                            "size": "xs",
                            "wrap": True,
                            "margin": "lg"
                        },
                        {
                            "type": "text",
                            "text": "【 會員回饋 】",
                            "weight": "bold",
                            "size": "md",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "商家徽章",
                                "size": "sm",
                                "margin": "none",
                                "color": "#AAAAAA",
                                "wrap": True,
                                "adjustMode": "shrink-to-fit",
                                "align": "start",
                                "offsetEnd": "none"
                            },
                            {
                                "type": "text",
                                "text": "我們會給予商家不同等級的徽章，並曝光於網頁及搜尋結果上",
                                "wrap": True,
                                "size": "sm",
                                "offsetStart": "none"
                            }
                            ],
                            "margin": "lg",
                            "spacing": "none"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "搜尋引擎推播",
                                "size": "sm",
                                "margin": "none",
                                "color": "#AAAAAA",
                                "wrap": True,
                                "adjustMode": "shrink-to-fit",
                                "align": "start",
                                "offsetEnd": "none"
                            },
                            {
                                "type": "text",
                                "text": "優先顯示於搜尋引擎的搜尋結果上",
                                "wrap": True,
                                "size": "sm",
                                "offsetStart": "none"
                            }
                            ],
                            "margin": "md",
                            "spacing": "none"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "優惠刊登",
                                "size": "sm",
                                "margin": "none",
                                "color": "#AAAAAA",
                                "wrap": True,
                                "adjustMode": "shrink-to-fit",
                                "align": "start",
                                "offsetEnd": "none"
                            },
                            {
                                "type": "text",
                                "text": "我們將會把商家的優惠刊登至 LINE SPOT，讓使用者一目了然",
                                "wrap": True,
                                "size": "sm",
                                "offsetStart": "none"
                            }
                            ],
                            "margin": "md",
                            "spacing": "none"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "特別企劃",
                                "size": "sm",
                                "margin": "none",
                                "color": "#AAAAAA",
                                "wrap": True,
                                "adjustMode": "shrink-to-fit",
                                "align": "start",
                                "offsetEnd": "none"
                            },
                            {
                                "type": "text",
                                "text": "我們將根據各間商家性質，為其推出特別企劃",
                                "wrap": True,
                                "size": "sm",
                                "offsetStart": "none"
                            }
                            ],
                            "margin": "md",
                            "spacing": "none"
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "（本功能與 LINE PAY 洽談中 ... ）",
                                "size": "sm"
                            }
                            ]
                        }
                        ]
                    }
                    }
                ]
                }


    
    #z = json.dumps(content)
    return content