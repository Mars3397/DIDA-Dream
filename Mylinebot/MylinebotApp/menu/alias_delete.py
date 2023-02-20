import requests
import json
import sys

headers = {"Authorization":"Bearer VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU="}
params = {
    "richMenuAliasId": sys.argv[1]
}

req = requests.request('DELETE', 'https://api.line.me/v2/bot/richmenu/alias/' + sys.argv[1], headers=headers, params=json.dumps(params).encode('utf-8'))
# x = req.text.split("\"")
print(req)

