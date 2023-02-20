import requests

headers = {"Authorization":"Bearer VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU="}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-266d58ae7a85dd2d324ef85a6b742d75', headers=headers)

print(req.text)