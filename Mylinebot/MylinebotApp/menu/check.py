from linebot import (
    LineBotApi, WebhookHandler
)


line_bot_api = LineBotApi('token')

rich_menu_list = line_bot_api.get_rich_menu_list()


for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)

