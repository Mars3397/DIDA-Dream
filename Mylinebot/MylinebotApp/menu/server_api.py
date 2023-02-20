import requests
import json

# headers = {"Authorization":"Bearer IwMBUQTWWJoR94mrOpONfz7IOuMeZRDhi35qJvxQZB444gO/RXQbWFvSc70cw4QdZ5MYh74ENZBcB877FCtP2xHyNMjglSeaSjqrI/52XTuBvfaWuZa0vNsOAuC0Tut+D9Ic0BoOEV/WUpiQo7aByo9PbdgDzCFqoOLOYbqAITQ=","Content-Type":"application/json"}
# datas = {
#     "view": {
#         "type": "tall",
#         "url": "https://www.youtube.com/"
#     },
#     "description": "youtube",
#     "features": {
#         "ble": True,
#         "qrCode": True
#     },
#     "permanentLinkPattern": "concat",
#     "scope": ["profile", "chat_message.write"],
#     "botPrompt": "none"
# }

# req = requests.request('POST', 'https://api.line.me/liff/v1/apps', headers=headers, data=json.dumps(datas).encode('utf-8'))
# x = req.text.split("\"")
# print(str(x[3]))

# -H "Content-Type: application/x-www-form-urlencoded" \
# --data-urlencode 'grant_type=client_credentials' \
# --data-urlencode 'client_id={channel ID}' \
# --data-urlencode 'client_secret={channel secret}'

headers = {"Content-Type":"application/x-www-form-urlencoded"}
datas = {
    "grant_type":"client_credentials",
    "client_id":"1657635549",
    "client_secret":"fc319767ec0240561aee64c10f5cf65c"
}
req = requests.request('POST', 'https://api.line.me/v2/oauth/accessToken', headers=headers, data=datas)
print(req.text)

# print(req.text)

# curl -v -X POST https://api.line.me/v2/oauth/accessToken \
# -H "Content-Type: application/x-www-form-urlencoded" \
# --data-urlencode 'grant_type=client_credentials' \
# --data-urlencode 'client_id=Ub69b73b09d6997b61c675bac0af1808d' \
# --data-urlencode 'client_secret=fc319767ec0240561aee64c10f5cf65c'
