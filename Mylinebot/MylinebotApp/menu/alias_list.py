import requests
import json

headers = {"Authorization":"Bearer 'token'"}

req = requests.request('GET', 'https://api.line.me/v2/bot/richmenu/alias/list', headers=headers)
# x = req.text.split("\"")
print(req.text)

