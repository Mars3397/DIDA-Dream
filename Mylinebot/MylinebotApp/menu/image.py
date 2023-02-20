from linebot import (
    LineBotApi, WebhookHandler
)


line_bot_api = LineBotApi('token')

with open("image/store_shop.png", 'rb') as f:
    line_bot_api.set_rich_menu_image('richmenu-266d58ae7a85dd2d324ef85a6b742d75', "image/jpeg", f)