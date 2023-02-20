import requests
import json
import sys

headers = {"Authorization":"Bearer 'token'"}
params = {
    "richMenuAliasId": sys.argv[1]
}

req = requests.request('DELETE', 'https://api.line.me/v2/bot/richmenu/alias/' + sys.argv[1], headers=headers, params=json.dumps(params).encode('utf-8'))
# x = req.text.split("\"")
print(req)

