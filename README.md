# DIDA Dream (即食予)

[English](#english) | [中文](#chinese)

# English

## Introduction

DIDA Dream is an award-winning social innovation project that tackles global food waste through technology. Recognized with the Second Place award at the 2022 LINE Fresh Competition in Taipei (among 250 competing teams), our solution demonstrates how technology can bridge the gap between surplus food and those in need.

Our project began with a simple yet powerful insight: "If we could reduce global food waste by just 1/4, we could feed everyone in the world." This inspiration led us to develop an integrated platform that connects convenience stores, local businesses, and communities through a [LINE Official Account](https://page.line.me/?accountId=195dceee).

Using PHP, Python, and cloud-based services, we've built a comprehensive system that:
- Consolidates near-expiry food data from convenience stores and local merchants
- Enables easy purchase and charitable donation of surplus food
- Creates a sustainable cycle of food redistribution

The project has evolved from a competition entry into a full-fledged solution that's making a real impact in reducing food waste and helping communities.

Complete project introduction: https://prezi.com/view/tweaIMQvrEdc4rFSVIEQ/

## How It Works

We gather information about near-expiry products through nationwide convenience store APIs and local business registration systems. Through our creative "You Are What You Eat" campaign, we attract customers and obtain user preferences for precise notifications, enhancing user engagement. Additionally, we've built an online donation platform integrated with LINE Gift, ensuring surplus food effectively reaches those in need. As our brand influence grows, we not only increase the sales of near-expiry products but also spread awareness of our mission, encouraging more people to participate in donations and helping families in need.

## Technical Architecture
![](https://i.imgur.com/oWAvGFq.png)

## Web File Structure

### Psychological Test (`psycho_test`)
- `start.php`: Initial page of the psychological test
- `test_page1-6.php`: Pages for questions 1-6
- `final.php`: Results page (with one-click sharing)
- `test.php`: Processes answers and stores them in database

### Profile Management
- `edit_shop.php`: Modify merchant profile
- `edit_user_php.php`: Modify personal profile

### Product Management (`shop.php`)
- `add_meal.php`: Add new products
- `delete_meal.php`: Remove products
- `shop_search.php`: Search specific products
- `edit_meal.php`: Modify product information

### My Near-Expiry Products (`leftovers_page.php`)
- `clear_meal.php`: One-click clear all near-expiry products
- `leftovers_search.php`: Search specific near-expiry products
- `update_quantity.php`: Update product quantity (+ / - buttons)

### Search Functions (`search_page.php`)
- `search.php`: Filter stores based on user criteria
- `select.php`: Display all near-expiry products from selected stores

### LINE Bot Integration
- `privacy_doc.html`: Privacy terms for DIDA Dream project
- `buygift.php`: Demonstration of food voucher purchase process (web prototype)

### Registration
- User registration: `register_page.php`
- Store registration: `register_shop.html`
- Supporting files:
  - `register.php`: Store new user information
  - `register_shop.php`: Store new merchant information

### Other Utilities
- `redirect.php`: Page redirection with user ID handling
- `connect.php`: phpMyAdmin database connection
- `set_uid.php`: Session user ID management
- `record.php`: Point card display (with sharing feature)

## LINE Bot Features

### Technical Overview
1. Customized Push Notifications: Server-side thread for scheduled notifications based on database information
2. Rich Menu: Multiple switchable rich menus using Rich Menu API, customized by user type
3. LINE LIFF: Web integration for direct access to personal information like LINE ID

### User Menu Features
- Product Search
- Benefit Map
- Friend Referral
- Profile Management
- Contact Support
- Food Voucher System
- Point Card
- Project Information

### Merchant Menu Features
- Product Management
- Membership System
- Profile Updates
- Support Contact
- Project Participation

### Requester Menu Features
- Product Search
- Benefit Map
- Friend Referral
- Profile Management
- Food Voucher Reception

---

# Chinese

## 專案簡介

即食予是一個獲獎的社會創新專案，運用科技解決全球食物浪費問題。在2022年台北LINE Fresh競賽中從250個參賽團隊中脫穎而出獲得第二名，展現了科技如何能夠有效地連結剩餘食物與需要幫助的人。

我們的專案源於一個簡單但深具意義的洞察：「只要全球減少1/4的食物浪費，就可以餵飽每個人」。這個想法促使我們開發了一個整合性平台，通過 [LINE官方帳號](https://page.line.me/?accountId=195dceee) 連結便利商店、在地商家和社區。

使用PHP、Python和雲端服務，我們建立了一個完整的系統，實現：
- 整合便利商店和在地商家的即期品資訊
- 便捷的購物和慈善捐贈機制
- 創造永續的食物重分配循環

這個專案已從競賽作品發展成為一個實際發揮影響力的解決方案，在減少食物浪費和幫助社區方面產生實質效益。

完整企劃介紹：https://prezi.com/view/tweaIMQvrEdc4rFSVIEQ/

## 運作方式

我們使用全台超商 API 及在地商家註冊系統取得即期品資訊。透過具創意的 You Are What You Eat 企劃，吸引客戶加入，
並藉此取得用戶偏好、精準推播，提升使用者黏著度。
同時，結合 LINE 禮物搭建線上捐贈平台，讓剩食有效地送到需要的人手中。
擴大品牌影響力後，不僅能提升即期品銷量，也讓理念被更多人看見，進而響應捐贈，以剩食為燈，點亮需要幫助的家庭。

# 技術架構圖
![](https://i.imgur.com/oWAvGFq.png)

# Web File Usage

- **心理測驗** `psycho_test`
    - `start.php`: 心理測驗之起始頁面
    - `test_page1.php`: 心理測驗第一題的頁面
    - `test_page2.php`: 心理測驗第二題的頁面
    - `test_page3.php`: 心理測驗第三題的頁面
    - `test_page4.php`: 心理測驗第四題的頁面
    - `test_page5.php`: 心理測驗第五題的頁面
    - `test_page6.php`: 心理測驗第六題的頁面
    - `final.php`: 顯示測驗結果的頁面（設有一鍵分享功能）
    - `test.php`: 處理各題問題之回答，並存到 database

- **個人資料＆商家資料** `edit_user.php`
    - `edit_shop.php`: 修改商家檔案
    - `edit_user_php.php`: 修改個人檔案

- **商品檔案** `shop.php`
    - `add_meal.php`: 新增商品到商品檔案
    - `delete_meal.php`: 將商品從商品檔案中移除
    - `shop_search.php`: 在商品檔案頁面中搜尋特定商品
    - `edit_meal.php`: 更改商品資訊

- **我的即期品** `leftovers_page.php`
    - `clear_meal.php`:  一鍵清除所有即期品
    - `leftovers_search.php`: 在我的即期品頁面中搜尋特定即期品
    - `update_quantity.php`: 更改即期品數量（按 + , - 按鈕的時候）

- **搜尋** `search_page.php`
    - `search.php`: 執行使用者設定之設定條件，篩選出符合條件的店家
    - `select.php`: 顯示所選店家的所有即期品

- **Line Bot**
    - `privacy_doc.html`: 參與即時予計畫之隱私權條款
    - `buygift.php`: 購買即時券的流程展示（網頁實作之 prototype）

- **註冊** `register_page.php` → 使用者、 `register_shop.html` → 店家
    - `register.php`: 將新註冊之使用者資訊存到 users 的資料庫
    - `register_shop.php`: 將新註冊之店家資訊存到 shops 的資料庫
    - `register_page1.php`: 讓使用者選擇欲註冊之身份（後來沒用了）
    - `register1.php`: 重新導向至欲註冊身份的填寫頁面

- **其他**
    - `redirect.php`: 根據網址 flag 將使用者重新導向至該頁面，同時將使用者 id 傳給 set_uid.php
    - `connect.php`: 連至 phpMyAdmin databas（包含資料庫 IP 等等）
    - `set_uid.php`: 將傳進來的 user id 存進 session
    - `record.php`: 展示集點卡頁面（設有一鍵分享功能）
    - `update.php`: 用來更新 s_id 讓他在 shops 跟 meals 的 database 都一致（用了一次就不需要了）

# LINEBot Usage
## 技術介紹
1. 客製化主動推播：在 server 內建立一條 thread，並設定根據資料庫的資料定期推播消息給使用者
2. 圖文選單：利用 Rich Menu API 來實現多個圖文選單切換，並且可以根據使用者身分設定每個人的選單形式
3. LINE LIFF：利用 LIFF API 讓網頁端可以直接獲取個人資料如 LINE ID 等等，可以省去 redirect 到網站的成本

## 使用者選單
### 主選單
![](https://i.imgur.com/2RUxQmj.png)
- 查詢即期品：根據使用者偏好、位置，客製化顯示出適合他的商家以及即期品品項
- 優惠地圖：預計可連結至 LINE SPOT 的優惠地圖
- 推薦給好友：可一鍵分享即食予官方帳號給好友
- 資料修改：連結至 edit_user.php 的頁面進行個人資料修改
- 聯絡我們：透過 flex message 顯示聯絡訊息

### 即食予
![](https://i.imgur.com/CtNq6bJ.png)
- 發送即食卷：連結到 LINE 禮物捐贈即食卷給 requesters，透過後端資料庫配對給需要的人
- 集點卡：連結到 record.php 顯示集點卡
- 支持我們：預計可連結至 LINE PAY
- 了解計畫：透過 flex message 大致介紹即時予計畫
   
## 商家選單
### 主選單
![](https://i.imgur.com/TIQKDbO.png)
- 商品修改：連結至 edit_meal.php 修改商品
- 加入會員：加入會員可享有會員回饋
- 資料修改：可一鍵分享即食予官方帳號給好友
- 聯絡我們：透過 flex message 顯示聯絡訊息

### 其他功能
![](https://i.imgur.com/YBdDWdv.png)
- 查詢即期品：根據使用者偏好、位置，客製化顯示出適合他的商家以及即期品品項
- 優惠地圖：預計可連結至 LINE SPOT 的優惠地圖
- 推薦給好友：可一鍵分享即食予官方帳號給好友

### 即食予
![](https://i.imgur.com/MASRRCL.png)
- 參與計畫：小商家加入即時予計畫的管道
- 了解計畫：透過 flex message 大致介紹即時予計畫
- 解鎖會員功能

## Requesters 選單
### 主選單
![](https://i.imgur.com/2RUxQmj.png)
- 查詢即期品：根據使用者偏好、位置，客製化顯示出適合他的商家以及即期品品項
- 優惠地圖：預計可連結至 LINE SPOT 的優惠地圖
- 推薦給好友：可一鍵分享即食予官方帳號給好友
- 資料修改：連結至 edit_user.php 的頁面進行個人資料修改
- 聯絡我們：透過 flex message 顯示聯絡訊息

### 即食予
![](https://i.imgur.com/B9kwZfw.png)
- 收取即食卷：透過後端資料庫配對收取捐贈者捐贈的即食卷
- 了解計畫：透過 flex message 大致介紹即時予計畫
