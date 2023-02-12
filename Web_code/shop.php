<?php 
include 'connect.php';

$stmt = $conn->prepare("select * from MylinebotApp_shops where u_id = :u_id");
$stmt->execute(array('u_id' => $_SESSION['u_id']));
$info = $stmt->fetch();
$_SESSION['s_id'] = $info['s_id'];

if ($_SESSION['search']) {
    $meal_info = $_SESSION['search'];
} else {
    $stmt = $conn->prepare("select * from MylinebotApp_meals where s_id = :s_id");
    $stmt->execute(array('s_id' => $info['s_id']));
    if ($stmt->rowCount() != 0) {
        $flag = true;
        $meal_info = $stmt->fetchAll(PDO::FETCH_ASSOC);
    } else $flag = false;
}

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
        <li><a href="edit_user.php">資料</a></li>
        <li class="active"><a href="shop.php">商品檔案</a></li>
        <li><a href="leftovers_page.php">我的即期品</a></li>
        <li><a href="search_page.php">搜尋</a></li>
        </ul>
        <div class="tab-content">
            <div id="menu1" class="tab-pane fade in active">
                <!-- Modal -->
                <div class="modal fade" id="add_meal" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true"> 
                    <div class="modal-dialog modal-sm">
                        <div class="modal-content glow bg">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal">&times;</button>
                                <h4 class="modal-title glow_light">新增即期品</h4>
                            </div>
                            <!-- add meal form -->
                            <form class="form-group" action="add_meal.php" method="post" Enctype="multipart/form-data">
                            <div class="row" style="margin-left: 10px; margin-right: 10px;">
                                <div class="col" style="margin-top: 15px;">
                                <label for="ex3">商品名稱</label>
                                <input class="form-control input" id="ex3" type="text" name="m_name" placeholder="請輸入商品名稱">
                                </div>
                            </div>
                            <div class="row" style="margin-top: 15px; margin-left: 10px; margin-right: 10px;">
                                <div class="col">
                                <label for="ex7">價格</label>
                                <input class="form-control input" id="ex7" type="number" name="m_price" placeholder="請輸入商品價格">
                                </div>
                            </div>
                            <div class="row" style="margin-left: 10px; margin-right: 10px; margin-top: 15px;">
                                <div class="col">
                                <label for="ex4">種類</label>
                                <select class="form-control input" id="m_group" name="m_group">
                                    <option>請選擇種類</option>
                                    <option>飯糰手捲</option>
                                    <option>飯類主食</option>
                                    <option>麵類主食</option>
                                    <option>湯品小吃</option>
                                    <option>三明治沙拉</option>
                                    <option>蔬果</option>
                                    <option>麵包甜點</option>
                                    <option>吐司蛋糕</option>
                                </select>
                                </div>
                            </div>
                            <div class="row" style="margin-left: 10px; margin-right: 10px; margin-top: 15px;">
                                <div class="col">
                                <button style=" margin-top: 15px;" type="submit" class="p btn">新增</button>
                                </div>
                            </div>
                            </form>
                        </div>
                    </div>
                </div>
                <!-- ------------------------------------------------------------------------------------- -->
                <div class="row">
                    <h3 class="glow_light col-xs-8 col-sm-10">商品檔案</h3>
                    <div class="col-xs-2"  style="margin-top: 20px;">
                    <button type="button" style="margin-left: 5px;" class="end p btn btn-secondary" data-toggle="modal" data-target="#add_meal">新增商品</button>
                    </div>
                </div>
                <!-- Serach -->
                <br>
                <form action="shop_search.php" method="post">
                    <div class="form-group">
                        <label class="control-label " for="m_name">搜尋商品</label>
                        <div class="row">
                            <div class="col-xs-6 col-sm-8">
                                <input type="text" class="form-control input" id="m_name" placeholder="輸入欲搜尋的商品名稱" name="input">
                            </div>
                            <div class="col-sm-1"></div>
                            <button type="submit" class="p btn btn-secondary" id="search_btn">搜尋</button>
                            <button type="submit" class="p btn btn-secondary" id="search_btn2">返回完整列表</button>
                        </div>
                    </div>
                </form>

                <div class="row" style="margin-left: 1px; margin-right: 1px">
                <div class="col">
                <table class="table" style=" margin-top: 15px;">
                    <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col" class="col-xs-4">餐點名稱</th>
                        <th scope="col">種類</th>
                        <th scope="col">價格</th>
                        <th scope="col"></th>
                        <th scope="col"></th>
                    </tr>
                    </thead>
                    <tbody>
                    <?php for ($i = 0; $i < count($meal_info); $i++): ?>
                    <tr>
                        <?php $str = str_replace(" ", "_", 'meal'.$meal_info[$i]['id']); ?>
                        <th scope="row"><?php echo $i + 1; ?></th>
                        <td><?php echo $meal_info[$i]['m_name']; ?></td>
                        <td><?php echo $meal_info[$i]['m_group']; ?></td>
                        <td><?php echo $meal_info[$i]['m_price']; ?></td>
                        <td><button type="button" class="p btn" data-toggle="modal" data-target="<?php echo '#' . $str; ?>">編輯</button></td>

                        <!-- Modal -->
                        <div class="modal fade" id="<?php echo $str; ?>" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                            <div class="modal-dialog black" role="document">
                                <div class="modal-content glow bg">
                                    <form action="edit_meal.php" method="post">
                                        <div class="modal-header">
                                            <h4 class="modal-title glow_light" id="staticBackdropLabel"><?php echo '編輯 '.$meal_info[$i]['m_name'].' 價格'; ?></h5>
                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                            <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div class="modal-body">
                                            <div class="row" style="margin-top: 15px; margin-left: 10px; margin-right: 10px;">
                                                <div class="col">
                                                    <label for="ex71">價格</label>
                                                    <input class="form-control input" id="ex71" type="number" name="new_price" placeholder="請輸入新的價格">
                                                </div>
                                                <input type="hidden" value="<?php echo $meal_info[$i]['id']; ?>" name="id">
                                            </div>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="submit" class="btn btn-default">編輯</button>    
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                        <td>
                            <form action="delete_meal.php" method="post">
                                <input type="hidden" value="<?php echo $meal_info[$i]['id']; ?>" name="id">
                                <button type="submit" class="p btn" name="delete">刪除</button>
                            </form>
                        </td>
                    </tr>
                    <?php endfor; ?>
                    </tbody>
                </table>
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

    <style> 
        body {
            background-color: #120f28;
        }

        .bg {
			background-color: #120f28;
			border: 1px solid #9E8C6A;
			border-radius: 10px;
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

        .glow_light {
            color: #fffae3;
            text-shadow: #fff 1px 0 30px;
            font-family: Garamond, serif;
        }

        .glow {
            color: #fffae3;
            font-family: Garamond, serif;
        }

        .black {
            color: black;
            font-family: Garamond, serif;
        }

        .input {
            background: #120f28;
            border: 1px solid #fffae3;
        }

        a {
            color: inherit;
        }

        .close {
            color: #fff; 
            opacity: 1;
        }

        #end {
            display: flex;
            justify-content: right;
        }
    </style>
</body>
</html>
