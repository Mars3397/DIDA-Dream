from linebot import (
    LineBotApi, WebhookHandler
)


line_bot_api = LineBotApi('VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU=')

with open("image/store_shop.png", 'rb') as f:
    line_bot_api.set_rich_menu_image('richmenu-266d58ae7a85dd2d324ef85a6b742d75', "image/jpeg", f)