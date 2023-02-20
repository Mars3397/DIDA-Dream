from linebot import (
    LineBotApi, WebhookHandler
)


line_bot_api = LineBotApi('VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU=')

rich_menu_list = line_bot_api.get_rich_menu_list()


for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)

