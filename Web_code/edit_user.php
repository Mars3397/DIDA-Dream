<?php 
include 'connect.php';
$u_id = $_SESSION['u_id'];

# fetch user info
$stmt = $conn->prepare("select * from MylinebotApp_users where u_id = :u_id");
$stmt->execute(array('u_id' => $u_id));
$info = $stmt->fetch();

$stmt_shop = $conn->prepare("select * from MylinebotApp_favor_shop where u_id = :u_id");
$stmt_shop->execute(array('u_id' => $u_id));
$info_shop = $stmt_shop->fetchAll(PDO::FETCH_ASSOC);

$stmt_food = $conn->prepare("select * from MylinebotApp_favor_food where u_id = :u_id");
$stmt_food->execute(array('u_id' => $u_id));
$info_food = $stmt_food->fetchAll(PDO::FETCH_ASSOC);

$stmt_time = $conn->prepare("select * from MylinebotApp_favor_time where u_id = :u_id");
$stmt_time->execute(array('u_id' => $u_id));
$info_time = $stmt_time->fetchAll(PDO::FETCH_ASSOC);

$stmt = $conn->prepare("select * from MylinebotApp_shops where u_id = :u_id");
$stmt->execute(array('u_id' => $_SESSION['u_id']));
$shop_info = $stmt->fetch();

?>

<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <!-- Bootstrap CSS -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <title>DIDA Dream</title>
</head>

<body>
  <div class="container glow" style="margin-top: 10px;">
    <ul class="nav nav-tabs">
        <li class="active"><a href="edit_user.php">資料</a></li>
        <?php if ($info['u_role'] == 's') : ?>
          <li><a href="shop.php">商品檔案</a></li>
          <li><a href="leftovers_page.php">我的即期品</a></li>
        <?php endif;?>
        <li><a href="search_page.php">搜尋</a></li>
    </ul>

    <div class="tab-content">
      <div id="home" class="tab-pane fade in active">
      <?php if ($info['u_role'] == 's') : ?>
        <div>
          <h3 class="glow_light">店家資訊</h3>
          <br>
          <p>店家名稱：<?php echo $shop_info['s_name'] ?></p>
          <br>
          <p>店家類別：<?php echo $shop_info['s_category'] ?></p>
          <br>
          <p>店家地址：<?php echo $shop_info['s_address'] ?></p>
          <br>
          <p>會員等級：<?php echo $shop_info['s_level'] ?></p>
          <br>
          <p>營業時間：<?php echo $shop_info['s_start_time'].' ~ '.$shop_info['s_end_time'] ?></p>
          <br>
          <p>營業日：<?php 
          print "星期";
            if (substr($shop_info['s_openday'], 0, 1) == "1") {
              print "一 ";
            }
            if (substr($shop_info['s_openday'], 1, 1) == "1") {
              print "二 ";
            }
            if (substr($shop_info['s_openday'], 2, 1) == "1") {
              print "三 ";
            }
            if (substr($shop_info['s_openday'], 3, 1) == "1") {
              print "四 ";
            }
            if (substr($shop_info['s_openday'], 4, 1) == "1") {
              print "五 ";
            }
            if (substr($shop_info['s_openday'], 5, 1) == "1") {
              print "六 ";
            }
            if (substr($shop_info['s_openday'], 6, 1) == "1") {
              print "日 ";
            }
          ?></p>
          <br>
          <button type="button" style="margin-left: 5px;" class="p btn btn-secondary" data-toggle="modal" data-target="#shop_profile">變更店家資訊</button>
          <!-- Modal -->
          <div class="modal fade" id="shop_profile" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true"> 
          <div class="modal-dialog">
              <div class="modal-content glow bg">
              <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal">&times;</button>
                  <h4 class="modal-title glow_light">變更店家資訊</h4>
              </div>
              <!-- add edit_shop.php -->
              <form action="edit_shop.php" method="post"> 
                  <div class="modal-body">
                  <div class="form-group">
                      <label class="control-label" for="new_name" style="font-weight: bold;">店家名稱</label>
                      <input type="text" class="form-control input" id="new_name" placeholder="輸入新的店家名稱" name="new_name">
                  </div>
                  <div class="form-group">
                      <label class="control-label " for="new_type" style="font-weight: bold;">店家類別</label>
                      <select class="form-control input" id="new_type" name="new_type">
                          <!-- <option>請選擇類別</option> -->
                          <option>全家</option>
                          <option>7-11</option>
                          <option>麵包店</option>
                      </select>
                  </div>
                  <div class="form-group">
                      <label class="control-label " for="new_address" style="font-weight: bold;">店家地址</label>
                      <input type="text" class="form-control" id="new_shop_address" placeholder="輸入新的店家地址" name="new_address">
                      <input type="hidden" id="shop_lat" name="lat" value="">
							        <input type="hidden" id="shop_lon" name="lon" value="">
                  </div>
                  
                  <div class="form-group">
                    <label for="start" style="font-weight: bold;">開始營業時間：</label>
                    <input type="time" id="start" name="start" style="color: black; width: 50%">
                  </div>
                  <div class="form-group">
                    <label for="end" style="font-weight: bold;">結束營業時間：</label>
                    <input type="time" id="end" name="end" style="color: black; width: 50%">
                  </div>
                  <div class="form-group">
                    <label style="font-weight: bold;">營業日：</label><br>
                    <div>
                      <div>
                        <input type="checkbox" name="s_openday" value="ㄧ" id="mon"/>
                        <label for="mon" style="margin-right: 5px;">星期一 </label>
                        <input type="checkbox" name="s_openday" value="二" id="tue"/>
                        <label for="tue" style="margin-right: 5px;">星期二 </label>
                        <input type="checkbox" name="s_openday" value="三" id="wed"/>
                        <label for="wed" style="margin-right: 5px;">星期三 </label>
                        <input type="checkbox" name="s_openday" value="四" id="tur"/>
                        <label for="tur" style="margin-right: 5px;">星期四 </label>
                      </div>
                      <div>
                        <input type="checkbox" name="s_openday" value="五" id="fri"/>
                        <label for="fri" style="margin-right: 5px;">星期五 </label>
                        <input type="checkbox" name="s_openday" value="六" id="sat"/>
                        <label for="sat" style="margin-right: 5px;">星期六 </label>
                        <input type="checkbox" name="s_openday" value="日" id="sun"/>
                        <label for="sun" style="margin-right: 5px;">星期日 </label>
                      </div>
                    </div>
                  </div>
                  </div>
                  <div class="modal-footer">
                  <button type="submit" class="btn btn-default">變更</button>
                  </div>
              </form>
              </div>
            </div>
            </div>
        </div>
        <!-- -------------------------------------------------------------------------- -->
        <br>
        <hr>
      <?php endif; ?>
      <?php if ($info['u_role'] == 'u') : ?>
        <h3 class="glow_light">個人資料</h3>
        <div class="row">
          <div class="col-xs-10">
            <br>
            <p>LINE 名稱：<?php echo $info['u_name'] ?></p>
            <br>
            <p>關注店家：
              <?php
                for($i=0; $i < count($info_shop); $i++){
                  echo $info_shop[$i]['s_category'];
                  echo "  ";
                }
              ?>
            </p>
            <br>
            <p>喜好品項：
              <?php
                for($i=0; $i < count($info_food); $i++){
                  echo $info_food[$i]['m_group'];
                  echo "  ";
                }
              ?>
            </p>
            <br>
            <p>通知時間：
              <?php
                for($i=0; $i < count($info_time); $i++){
                  echo $info_time[$i]['f_time'];
                  echo "  ";
                }
              ?>
            </p>
            <br>
            <p>地址：<?php echo $info['u_address'] ?></p>
            <br>
            <p>位置：<?php echo $info['u_longtitude'].' , '.$info['u_latitude'] ?></p>
            <br>
            <p>累積捐贈金額：<?php echo $info['u_give'] ?></p>
            <br>
            <button type="button " style="margin-left: 5px;" class=" btn p" data-toggle="modal" data-target="#location">更改個人資料</button>
            <br><br><br><br>

            <!-- Modal -->
            <div class="modal fade black" id="location" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true"> 
            <div class="modal-dialog modal-sm">
                <div class="modal-content bg glow">
                  <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                    <h4 class="modal-title glow_light">變更個人資料</h4>
                  </div>
                  <form action="edit_user_php.php" method="post">
                    <div class="modal-body">
                      <input type="hidden" value="<?php echo $info['u_name']; ?>" name="u_name">
                      <div class="form-group">
                        <label style="font-weight: bold;">想收到哪裡的即期品資訊：</label><br>
                        <div>
                          <input type="checkbox" name="use_address" value="now" id="now"/>
                          <label for="now" style="margin-right: 5px;">直接使用現在位置 </label>
                        </div>
                        <div>
                          <input type="checkbox" name="use_address" value="keyin" id="keyin"/>
                          <label for="keyin" style="margin-right: 5px;">手動輸入（請填寫下方欄位） </label>
                        </div>
                        <input type="text" style="border-bottom: 1px solid #fffae3; color: white;" class="form-control input" id="u_address" autocomplete="off" name="address" placeholder="以地標或地址填寫">
                        <input type="hidden" id="u_lat" name="lat" value="">
                        <input type="hidden" id="u_lon" name="lon" value="">
                      </div>

                      <!-- <label>請選擇身份：</label><br>
                      <select name="u_role" class="from-control input">
                        <option value="u">一般使用者</option> 
                        <option value="s">商家</option> 
                      </select>
                      <br><br> -->

                      <label style="font-weight: bold;">請選擇喜歡的店家：</label><br>
                      <input type="checkbox" name="s_category[]" value="7-11" id="7-11"/>
                      <label for="7-11" style="margin-right: 5px;">7-11 </label>
                      <input type="checkbox" name="s_category[]" value="全家" id="f"/>
                      <label for="f" style="margin-right: 5px;">全家 </label>
                      <input type="checkbox" name="s_category[]" value="麵包店" id="b"/>
                      <label for="b" style="margin-right: 5px;">麵包店 </label>
                      <br><br>
                      <label style="font-weight: bold;">喜歡的品項：</label><br>
                      <div>
                        <input type="checkbox" name="m_group[]" value="飯糰手卷" id="rb"/>
                        <label for="rb" style="margin-right: 5px;">飯糰手卷 </label>
                        <input type="checkbox" name="m_group[]" value="飯類主食" id="r"/>
                        <label for="r" style="margin-right: 5px;">飯類主食 </label>
                        <input type="checkbox" name="m_group[]" value="麵類主食" id="n"/>
                        <label for="n" style="margin-right: 5px;">麵類主食 </label>
                      </div>
                      <div>
                        <input type="checkbox" name="m_group[]" value="湯品小吃" id="s"/>
                        <label for="s" style="margin-right: 5px;">湯品小吃 </label>
                        <input type="checkbox" name="m_group[]" value="三明治沙拉" id="sa"/>
                        <label for="sa" style="margin-right: 5px;">三明治沙拉 </label>
                        <input type="checkbox" name="m_group[]" value="蔬果" id="fr"/>
                        <label for="fr" style="margin-right: 5px;">蔬果 </label>
                      </div>
                      <div>
                        <input type="checkbox" name="m_group[]" value="麵包甜點" id="d"/>
                        <label for="d" style="margin-right: 5px;">麵包甜點 </label>
                        <input type="checkbox" name="m_group[]" value="吐司蛋糕" id="t"/>
                        <label for="t" style="margin-right: 5px;">吐司蛋糕 </label>
                      </div>
                      <br>
                      <label style="font-weight: bold;">想收到通知的時間：</label><br>
                      <input type="checkbox" name="f_time[]" value="10" id="10"/>
                      <label for="10" style="margin-right: 5px;">10:00 </label>
                      <input type="checkbox" name="f_time[]" value="17" id="17"/>
                      <label for="17" style="margin-right: 5px;">17:00 </label>
                      <input type="checkbox" name="f_time[]" value="20" id="20"/>
                      <label for="20" style="margin-right: 5px;">20:00 </label>
                      <br><br>
                    <div class="modal-footer">
                      <button type="submit" class="btn btn-default">變更</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>

          <?php endif; ?>

        </div>
      </div>
    </div>
  </div>

  <script>
    $(document).ready(function () {
      $(".nav-tabs a").click(function () {
        $(this).tab('show');
      });
    });
  </script>

  <script
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBKaRPTrJub0mPX86F8q_DBSpV8zQs56xM"
    defer
  ></script>

  <script src="https://static.line-scdn.net/liff/edge/2/sdk.js"></script>

	<script>
		$(document).ready(function() {
			$("#new_shop_address").on('input', function() {
				var address = document.getElementById('new_shop_address').value;

				if (address != '') {
					var geocoder = new google.maps.Geocoder();
					geocoder.geocode( { 'address': address }, function(results, status) {
						if (status == 'OK') {
							document.getElementById('shop_lat').value = results[0].geometry.location.lat();
							document.getElementById('shop_lon').value = results[0].geometry.location.lng();
						}
					});
				}
			});
		});

    $(document).ready(function() {
			$("#u_address").on('input', function() {
				var address = document.getElementById('u_address').value;

				if (address != '') {
					var geocoder = new google.maps.Geocoder();
					geocoder.geocode( { 'address': address }, function(results, status) {
						if (status == 'OK') {
							document.getElementById('u_lat').value = results[0].geometry.location.lat();
							document.getElementById('u_lon').value = results[0].geometry.location.lng();
						}
					});
				}
			});
		});
	</script>

  <style> 
    body {
        background-color: #120f28;
    }

    .bg {
			background-color: #120f28;
			border: 1px solid #9E8C6A;
			border-radius: 10px;
		}

    .glow_light {
        color: #fffae3;
        text-shadow: #fff 1px 0 30px;
        font-family: Garamond, serif;
        /* text-align: center; */
    }

    .glow {
        color: #fffae3;
        font-family: Garamond, serif;
    }

    .black {
        color: black;
        font-family: Garamond, serif;
    }

    .form-control {
        background: #120f28;
        border: none;
        border-bottom: 1px solid #fffae3;
    }

    .input {
        background: #120f28;
        border: none;
        border-bottom: 1px solid #fffae3;
    }

    a {
      color: inherit;
    }

    .p {
      font-family: Garamond, serif;
      background-color: #120f28;
      border: 1px solid #9E8C6A;
    }

    .p:hover {
      color: black;
      font-family: Garamond, serif;
      background-color: #d4d4d4;
      border: 1px solid white;
    }

    .close {
      color: #fff; 
      opacity: 1;
    }
  </style>

</body>
</html>