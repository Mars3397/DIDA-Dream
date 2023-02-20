import requests

headers = {"Authorization":"Bearer 'token'"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-266d58ae7a85dd2d324ef85a6b742d75', headers=headers)

print(req.text)