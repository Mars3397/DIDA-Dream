from linebot import (
    LineBotApi, WebhookHandler
)
import sys



line_bot_api = LineBotApi('token')

rich_menu_list = line_bot_api.get_rich_menu_list()

line_bot_api.delete_rich_menu(sys.argv[1])


