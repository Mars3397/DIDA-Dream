import requests
import json
import sys

headers = {"Authorization":"Bearer 'token'","Content-Type":"application/json"}
datas = {
    "richMenuAliasId": sys.argv[1],
    "richMenuId": sys.argv[2]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', headers=headers, data=json.dumps(datas).encode('utf-8'))
# x = req.text.split("\"")
print(req)

