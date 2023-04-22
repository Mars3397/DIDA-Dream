from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from MylinebotApp.models import *


from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction,
    FlexSendMessage,
    ImageSendMessage,
    BeaconEvent,
    FollowEvent
)

import subprocess
import requests
import time
import threading
import json
from MylinebotApp.template.check_food import check_food
from MylinebotApp.template.update_info import update_info
from MylinebotApp.template.update_info_shop import update_info_shop
from MylinebotApp.template.update_info_requester import update_info_requester
from MylinebotApp.template.donate import donate
from MylinebotApp.template.already_donated import already_donated
from MylinebotApp.template.shop_update_info import shop_update_info
from MylinebotApp.template.insert_meals import insert_meals
from MylinebotApp.template.welcome import welcome
from MylinebotApp.template.user_FAQ import user_FAQ
from MylinebotApp.template.share_to_friend import share_to_friend
from MylinebotApp.template.shop_sop import shop_sop
from MylinebotApp.template.receive_gift import receive_gift
from MylinebotApp.template.check_food_title import check_food_title
from MylinebotApp.template.test import test
from MylinebotApp.template.shop_FAQ import shop_FAQ
from MylinebotApp.template.membership import membership
from MylinebotApp.template.support_us import support_us
from django.shortcuts import render
import math
from MylinebotApp.familys import family_table
import random

#import MylinebotApp.menu.menu_user_menu 

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
headers = {"Authorization":"Bearer VgIDgAR2eSjJ5IH84TxE0l6lK651Oi5c9St+VaONUhvmjpDIRvJKzKQ+CYoQPESy9MvIqpJW2zTfen9MR0dg5FJLEOejNZ9tZImQfTSZ57Ot+r3ZjAdIsEciGvuazq5tPhF+KRCxXKyxH5ju+WymswdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
menu_user_menu = 'richmenu-64a1e7982838d09960219d1a732dd7ca' # richmenu-64a1e7982838d09960219d1a732dd7ca
menu_requester_menu = 'richmenu-17cd9ac40ced87a9ad9d0e2373313b08'
menu_shop_menu_pro_none = 'richmenu-79d13b35327ddc48847ddca3dcfec804'


def index(request):
    day = 29
    post_title = '[Day 29]用Django架構建置專屬的LINEBOT吧 - LIFF(II)template與LIFF'
    return render(request,'IT_help/index.html',locals())

def push_message():
    while True:
        localtime = time.localtime()
        result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
        if result=="2023-01-14 12:41:00 PM":
            user_info = users.objects.all()
            for user in user_info:
                meals_name = []
                meals_quantity = []
                shop_name = []
                shop_category = []
                m_number = []
                shop_star = ['4.1','4.2','4.4','4.7','4.8']
                shop_level = ['1','2','3','4','2']
                favor_food_list = []
                
                shop_distance = {}
                message = []
                family_shop_info = favor_food.objects.filter(u_id=user.u_id)
                all_shop = shops.objects.all()
                for favor_foods in family_shop_info:
                    favor_food_list.append(favor_foods.m_group)
                count = 1
                # family_table
                for shop in family_table:
                    p = []
                    if user.u_latitude == 0 and user.u_longtitude == 0:
                        p = [25.0770622,121.5751213]
                    else:
                        p = [float(user.u_latitude),float(user.u_longtitude)]
                    q = [float(shop[1]),float(shop[2])]
                    shop_distance[shop[0]] = math.dist(p, q)
                    count = count + 1

                sorted_shop = sorted(shop_distance.items(), key=lambda x:x[1])
                visited_shop_number = 0
                while visited_shop_number < 5:
                    family_shop_info = family_shops.objects.filter(s_name=sorted_shop[visited_shop_number][0])
                    if len(family_shop_info) == 0:
                        visited_shop_number = visited_shop_number + 1
                        continue
                    for family_shop in family_shop_info:
                        print(family_shop.s_id)
                        if visited_shop_number == 5:
                            break
                        shop_info = meals.objects.filter(s_id=family_shop.s_id)
                        shop_category.append("全家")
                        shop_name.append(family_shop.s_name)
                        visited_food_number = 0
                        for product in shop_info:
                            if visited_food_number == 5:
                                break
                            if product.m_group in favor_food_list:
                                meals_name.append(product.m_name)
                                meals_quantity.append(product.m_quantity)
                                visited_food_number = visited_food_number + 1
                        if visited_food_number != 5:
                            for product in shop_info:
                                if visited_food_number == 5:
                                    break
                                meals_name.append(product.m_name)
                                meals_quantity.append(product.m_quantity)
                                visited_food_number = visited_food_number + 1
                        m_number.append(visited_food_number)
                        visited_shop_number = visited_shop_number + 1
                content = check_food(shop_name, shop_category, shop_star, shop_level, m_number, meals_name, meals_quantity)
                content2 = check_food_title()
                print(content2)
                if user.u_result == '辣椒': # 又水逆了嗎？點進來獲得好運吧 ୧( ˙ᵕ˙ )୨
                    message.append(FlexSendMessage(alt_text='快點進來，讓即食予溫暖你的心(  ˶ˊᵕˋ)੭♡',contents=content))  
                    message.append(FlexSendMessage(alt_text='快點進來，讓即食予溫暖你的心(  ˶ˊᵕˋ)੭♡', contents=content2))  
                elif user.u_result == '青椒':
                    message.append(FlexSendMessage(alt_text='又水逆了嗎？點進來獲得好運吧 ୧( ˙ᵕ˙ )୨',contents=content))  
                    message.append(FlexSendMessage(alt_text='又水逆了嗎？點進來獲得好運吧 ୧( ˙ᵕ˙ )୨', contents=content2))  
                elif user.u_result == '奇異果': # 即期品也瘋狂，就缺你一個 ʸᵉᵃʰ ٩( ᐖ )و
                    message.append(FlexSendMessage(alt_text='即期品也瘋狂，就缺你一個 ʸᵉᵃʰ ٩( ᐖ )و',contents=content))  
                    message.append(FlexSendMessage(alt_text='即期品也瘋狂，就缺你一個 ʸᵉᵃʰ ٩( ᐖ )و', contents=content2))  
                else:
                    index = random.randint(0,2)
                    if index == 0:
                        message.append(FlexSendMessage(alt_text='快點進來，讓即食予溫暖你的心(  ˶ˊᵕˋ)੭♡',contents=content))  
                        message.append(FlexSendMessage(alt_text='快點進來，讓即食予溫暖你的心(  ˶ˊᵕˋ)੭♡', contents=content2))  
                    elif index == 1:
                        message.append(FlexSendMessage(alt_text='又水逆了嗎？點進來獲得好運吧 ୧( ˙ᵕ˙ )୨',contents=content))  
                        message.append(FlexSendMessage(alt_text='又水逆了嗎？點進來獲得好運吧 ୧( ˙ᵕ˙ )୨', contents=content2))  
                    else:
                        message.append(FlexSendMessage(alt_text='即期品也瘋狂，就缺你一個 ʸᵉᵃʰ ٩( ᐖ )و',contents=content))  
                        message.append(FlexSendMessage(alt_text='即期品也瘋狂，就缺你一個 ʸᵉᵃʰ ٩( ᐖ )و', contents=content2))  
                line_bot_api.push_message(user.u_id,message)
            time.sleep(2)

def store_food_to_db():
    while True:
        localtime = time.localtime()
        result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
        if result=="2023-01-12 10:00:00 PM":
            p = subprocess.Popen("python3 ~/Mylinebot/MylinebotApp/write_to_db_2.py", shell=True)
            time.sleep(2)

def check_role():
    user_information = {}
    while True:
        user_info = users.objects.all()
        for user in user_info:
            if user.u_id not in user_information.keys():
                user_information[user.u_id] = user.u_role
                continue
            if user_information[user.u_id] != user.u_role:
                user_information[user.u_id] = user.u_role
                if user.u_role == 'u':
                    # delete_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu'
                    # req = requests.request('DELETE', delete_url, headers=headers)
                    post_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu/' + menu_user_menu
                    req = requests.request('POST', post_url, headers=headers)
                elif user.u_role == 's':
                    # delete_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu'
                    # req = requests.request('DELETE', delete_url, headers=headers)
                    post_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu/' + menu_shop_menu_pro_none
                    req = requests.request('POST', post_url, headers=headers)

threading.Thread(target=push_message).start()
threading.Thread(target=store_food_to_db).start()
threading.Thread(target=check_role).start()

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext=event.message.text
                uid=event.source.user_id
                profile=line_bot_api.get_profile(uid)
                name=profile.display_name
                pic_url=profile.picture_url
                points=0

                message=[]
                #if event.message.text=='開始遊戲':
                if users.objects.filter(u_id=uid).exists()==False:
                    users.objects.create(u_id=uid,u_name=name)
                    user_info = users.objects.filter(u_id=uid)
                    for user in user_info:
                        
                        content = welcome(uid)
                        
                        post_url = 'https://api.line.me/v2/bot/user/' + uid + '/richmenu/' + menu_user_menu
                        
                        req = requests.request('POST', post_url, headers=headers)
                        
                    message.append(FlexSendMessage(alt_text='歡迎加入即食雨',contents=content)) 
                else:
                    #message.append(TextSendMessage(text='已註冊'))
                    if event.message.text=='輸出會員資料':
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            info = 'UID=%s\nNAME=%s\n'%(user.u_id,user.u_name)
                            message.append(TextSendMessage(text=info))
                    elif event.message.text=='切換成使用者':
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            #DELETE https://api.line.me/v2/bot/user/{userId}/richmenu
                            #POST https://api.line.me/v2/bot/user/{userId}/richmenu/{richMenuId}
                            # delete_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu'
                            # req = requests.request('DELETE', delete_url, headers=headers)
                            
                            post_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu/' + menu_user_menu
                            req = requests.request('POST', post_url, headers=headers)
                            info = '已切換成使用者模式'
                            message.append(TextSendMessage(text=info))
                    elif event.message.text=='切換成requesters':
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            #DELETE https://api.line.me/v2/bot/user/{userId}/richmenu
                            #POST https://api.line.me/v2/bot/user/{userId}/richmenu/{richMenuId}
                            # delete_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu'
                            # req = requests.request('DELETE', delete_url, headers=headers)
                            post_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu/' + menu_requester_menu
                            req = requests.request('POST', post_url, headers=headers)
                            info = '已切換成requesters模式'
                            message.append(TextSendMessage(text=info))
                    # elif event.message.text=='miamia':
                    #     user_info = users.objects.filter(u_id=uid)
                    #     for user in user_info:
                    #         #DELETE https://api.line.me/v2/bot/user/{userId}/richmenu
                    #         #POST https://api.line.me/v2/bot/user/{userId}/richmenu/{richMenuId}
                    #         # delete_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu'
                    #         # req = requests.request('DELETE', delete_url, headers=headers)
                    #         post_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu/' + menu_requester_menu
                    #         req = requests.request('POST', post_url, headers=headers)
                    #         info = '認證成功'
                    #         message.append(TextSendMessage(text=info))
                    elif event.message.text=='切換成商家':
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            #DELETE https://api.line.me/v2/bot/user/{userId}/richmenu
                            #POST https://api.line.me/v2/bot/user/{userId}/richmenu/{richMenuId}
                            # delete_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu'
                            # req = requests.request('DELETE', delete_url, headers=headers)
                            post_url = 'https://api.line.me/v2/bot/user/' + user.u_id + '/richmenu/' + menu_shop_menu_pro_none
                            req = requests.request('POST', post_url, headers=headers)
                            info = '已切換成商家模式'
                            message.append(TextSendMessage(text=info))
                    elif event.message.text=='查詢即期品': 
                        user_info = users.objects.filter(u_id=uid)
                        meals_name = []
                        meals_quantity = []
                        shop_name = []
                        shop_category = []
                        shop_star = ['4.5','5','4.6','4.7','4.8']
                        shop_level = ['1','2','3','4','2']
                        m_number = []
                        favor_food_list = []
                        shop_distance = {}

                        for user in user_info:
                            family_shop_info = favor_food.objects.filter(u_id=user.u_id)
                            all_shop = shops.objects.all()
                            for favor_foods in family_shop_info:
                                favor_food_list.append(favor_foods.m_group)
                            count = 1
                            # family_table
                            for shop in family_table:
                                p = []
                                if user.u_latitude != 0 and user.u_longtitude != 0:
                                    p = [float(user.u_latitude),float(user.u_longtitude)]
                                else:
                                    p = [25.0770622,121.5751213]
                                q = [float(shop[1]),float(shop[2])]
                                shop_distance[shop[0]] = math.dist(p, q)
                                count = count + 1
                                # print(count)
                                # print([shop.s_name,shop.s_latitude,shop.s_longtitude],',')

                            sorted_shop = sorted(shop_distance.items(), key=lambda x:x[1])
                            visited_shop_number = 0
                            while visited_shop_number < 5:
                                family_shop_info = family_shops.objects.filter(s_name=sorted_shop[visited_shop_number][0])
                                # print(visited_shop_number)
                                # print(sorted_shop[visited_shop_number])
                                if len(family_shop_info) == 0:
                                    visited_shop_number = visited_shop_number + 1
                                    continue
                                for family_shop in family_shop_info:
                                    print(family_shop.s_id)
                                    print("haha")
                                    if visited_shop_number == 5:
                                        break
                                    shop_info = meals.objects.filter(s_id=family_shop.s_id)
                                    shop_category.append("全家")
                                    shop_name.append(family_shop.s_name)
                                    visited_food_number = 0
                                    for product in shop_info:
                                        if visited_food_number == 5:
                                            break
                                        if product.m_group in favor_food_list:
                                            meals_name.append(product.m_name)
                                            meals_quantity.append(product.m_quantity)
                                            visited_food_number = visited_food_number + 1
                                    if visited_food_number != 5:
                                        for product in shop_info:
                                            if visited_food_number == 5:
                                                break
                                            meals_name.append(product.m_name)
                                            meals_quantity.append(product.m_quantity)
                                            visited_food_number = visited_food_number + 1
                                    m_number.append(visited_food_number)
                                    visited_shop_number = visited_shop_number + 1

                                       
                        content = check_food(shop_name, shop_category, shop_star, shop_level, m_number, meals_name, meals_quantity)

                        message.append(FlexSendMessage(alt_text='查詢即期品',contents=content))  
                        emoji = [
                                    {
                                        "index": 23,
                                        "productId": "5ac21184040ab15980c9b43a",
                                        "emojiId": "222"
                                    },
                                    {
                                        "index": 46,
                                        "productId": "5ac21cc5031a6752fb806d5c",
                                        "emojiId": "132"
                                    }
                                ]
                        message.append(TextSendMessage(text='你知道嗎？只要送出一張即食券，就能照亮一個家庭$\n點擊選單的「即食予」，為剩食再分配盡一份力$', emojis=emoji))  

                    elif event.message.text=='資料修改': 
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            content2 = shop_sop(user.u_id)
                            message.append(FlexSendMessage(alt_text='商家資料SOP',contents=content2)) 
                    elif event.message.text=='推薦給好友': 
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            content = share_to_friend(user.u_id)
                        message.append(FlexSendMessage(alt_text='推薦給好友',contents=content))
                    elif event.message.text=='了解計畫':
                        image_message = ImageSendMessage(
                            original_content_url='https://2022.dida-dream.com/images/understand.PNG',
                            preview_image_url='https://2022.dida-dream.com/images/understand.PNG'
                        )
                        message.append(image_message)
                    elif event.message.text=='商家資料修改': 
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            content = shop_update_info(user.u_id)
                        message.append(FlexSendMessage(alt_text='商家資料修改',contents=content)) 
                    elif event.message.text=='商品修改': 
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            content = insert_meals(user.u_id)
                        message.append(FlexSendMessage(alt_text='商品修改',contents=content)) 
                    elif event.message.text=='加入會員' or event.message.text=='參與計畫' or event.message.text=='解鎖會員功能':
                        content = membership()
                        message.append(FlexSendMessage(alt_text='加入會員',contents=content)) 
                    elif event.message.text=='聯絡我們': 
                        user_info = users.objects.filter(u_id=uid)
                        for user in user_info:
                            if user.u_role == 'u':
                                content = user_FAQ()
                            elif user.u_role == 's':
                                content = shop_FAQ()
                        message.append(FlexSendMessage(alt_text='FAQ',contents=content)) 
                    elif event.message.text=='支持我們':
                        content = support_us()
                        message.append(FlexSendMessage(alt_text='test',contents=content))
                    elif event.message.text=='收取即食卷': 
                        user_info_requester = users.objects.filter(u_id=uid)
                        mapping_info = mapping.objects.all()
                        mapping_success = 0
                        already_queueing = 0
                        text=""
                        for map in mapping_info:
                            if map.ru_id==uid:
                                already_queueing = 1
                                break
                        if already_queueing == 0:
                            for map in mapping_info:
                                if map.stat=="g":
                                    user_info_giver = users.objects.filter(u_id=map.gu_id)
                                    mapping_success = 1
                                    for user in user_info_giver:
                                        text = text + user.u_name + '已收到愛心'
                                    # line_bot_api.push_message(map.gu_id,TextSendMessage(text=text))
                                    map.delete()
                                    break
                            if mapping_success == 0:
                                mapping.objects.create(ru_id=uid, stat="r")
                                text = '等待中...'
                                message.append(TextSendMessage(text=text))
                            else:
                                for user in user_info_giver:
                                    #text = '收到來自' + user.u_name + '的愛心'
                                    content = receive_gift()
                                    message.append(FlexSendMessage(alt_text='商品修改',contents=content)) 

                                    user_info = users.objects.filter(u_id=uid)
                                    meals_name = []
                                    meals_quantity = []
                                    shop_name = []
                                    shop_category = []
                                    shop_star = ['4.5','5','4.6','4.7','4.8']
                                    shop_level = ['1','2','3','4','2']
                                    m_number = []
                                    
                                    for user in user_info:
                                        visited_shop_number = 0
                                        family_shop_info = family_shops.objects.all()
                                        for family_shop in family_shop_info:
                                            if visited_shop_number == 5:
                                                break
                                            shop_info = meals.objects.filter(s_id=family_shop.s_id)
                                            shop_category.append("全家")
                                            shop_name.append(family_shop.s_name)
                                            visited_food_number = 0
                                            for product in shop_info:
                                                if visited_food_number == 5:
                                                    break
                                                meals_name.append(product.m_name)
                                                meals_quantity.append(product.m_quantity)
                                                visited_food_number = visited_food_number + 1
                                            m_number.append(visited_food_number)
                                            visited_shop_number = visited_shop_number + 1
                                    content = check_food(shop_name, shop_category, shop_star, shop_level, m_number, meals_name, meals_quantity)
                                    message.append(FlexSendMessage(alt_text='查詢即期品',contents=content))  
                                    
                        else:
                            text = '您已在等待中'
                            message.append(TextSendMessage(text=text))
                    elif event.message.text=='發送即食卷': 
                        user_info_giver = users.objects.filter(u_id=uid)
                        mapping_info = mapping.objects.all()
                        mapping_success = 0
                        already_queueing = 0
                        text=""
                        for map in mapping_info:
                            if map.stat=="r":
                                user_info_requester = users.objects.filter(u_id=map.ru_id)
                                mapping_success = 1
                                for user in user_info_requester:
                                    #text = text + '收到來自' + user.u_name + '的愛心'
                                    message.append(TextSendMessage(text="以下是附近有即期品的店家，提醒您要在期限內領取喔！")) 
                                    user_info = users.objects.filter(u_id=uid)
                                    meals_name = []
                                    meals_quantity = []
                                    shop_name = []
                                    shop_category = []
                                    shop_star = ['4.5','5','4.6','4.7','4.8']
                                    shop_level = ['1','2','3','4','2']
                                    m_number = []
                                    for user in user_info:
                                        visited_shop_number = 0
                                        family_shop_info = family_shops.objects.all()
                                        for family_shop in family_shop_info:
                                            if visited_shop_number == 5:
                                                break
                                            shop_info = meals.objects.filter(s_id=family_shop.s_id)
                                            shop_category.append("全家")
                                            shop_name.append(family_shop.s_name)
                                            visited_food_number = 0
                                            for product in shop_info:
                                                if visited_food_number == 5:
                                                    break
                                                meals_name.append(product.m_name)
                                                meals_quantity.append(product.m_quantity)
                                                visited_food_number = visited_food_number + 1
                                            m_number.append(visited_food_number)
                                            visited_shop_number = visited_shop_number + 1
                                    content = check_food(shop_name, shop_category, shop_star, shop_level, m_number, meals_name, meals_quantity)
                                    message.append(FlexSendMessage(alt_text='查詢即期品',contents=content))  
                                    
                                map.delete()
                                break
                        if mapping_success == 0:
                            mapping.objects.create(gu_id=uid, stat="g")
                            content = donate()
                            message.append(FlexSendMessage(alt_text='發送禮物',contents=content))  
                        else:
                            for user in user_info_requester:
                                text = user.u_name + '已收到愛心'
                                message.append(TextSendMessage(text=text))

                    else:
                        message.append(TextSendMessage(text='該功能尚在開發中'))
                line_bot_api.reply_message(event.reply_token,message)

                return HttpResponse()
            elif isinstance(event, PostbackEvent): 
                message = []
                if event.postback.data == "捐贈": 
                    content = already_donated()
                    message.append(FlexSendMessage(alt_text='感謝您的捐贈',contents=content)) 
                line_bot_api.reply_message(event.reply_token,message)
                return HttpResponse()
            elif isinstance(event, FollowEvent): 
                message = []
                uid=event.source.user_id
                profile=line_bot_api.get_profile(uid)
                name=profile.display_name
                users.objects.create(u_id=uid,u_name=name)
                user_info = users.objects.filter(u_id=uid)
                for user in user_info: 
                    content = welcome(uid)
                    post_url = 'https://api.line.me/v2/bot/user/' + uid + '/richmenu/' + menu_user_menu
                    req = requests.request('POST', post_url, headers=headers)
                message.append(FlexSendMessage(alt_text='歡迎加入即食雨',contents=content)) 

                line_bot_api.reply_message(event.reply_token,message)
                return HttpResponse()
            elif isinstance(event, BeaconEvent): 
                message = []
                message.append(TextSendMessage(text='beacon'))
                print(request.body)
                line_bot_api.reply_message(event.reply_token,message)
                return HttpResponse()
            else:
                return HttpResponseBadRequest()

