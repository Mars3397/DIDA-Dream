# 即食予 DIDA Dream

「只要全球減少 1/4 的食物浪費，就可以餵飽每個人」，我們由此發想「即食予」企劃，

透過整合即期品的 [LINE 官方帳號](https://page.line.me/?accountId=195dceee)，實現剩食再分配的目標。

我們使用全台超商 API 及在地商家註冊系統取得即期品資訊。透過具創意的 You Are What You Eat 企劃，吸引客戶加入，
並藉此取得用戶偏好、精準推播，提升使用者黏著度。
同時，結合 LINE 禮物搭建線上捐贈平台，讓剩食有效地送到需要的人手中。

擴大品牌影響力後，不僅提升即期品銷量，也讓理念被更多人看見，進而響應捐贈，以剩食為燈，點亮需要幫助的家庭。
<br/>

## Web File Usage

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