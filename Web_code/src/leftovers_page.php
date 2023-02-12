<?php 
include 'connect.php';

$stmt = $conn->prepare("select * from MylinebotApp_shops where u_id = :u_id");
$stmt->execute(array('u_id' => $_SESSION['u_id']));
$info = $stmt->fetch();
$_SESSION['s_id'] = $info['s_id'];

# fetch shop menu
$stmt = $conn->prepare("select * from MylinebotApp_meals where s_id = :s_id");
$stmt->execute(array('s_id' => $info['s_id']));
if ($stmt->rowCount() != 0) {
    $flag = true;
    $meal_info = $stmt->fetchAll(PDO::FETCH_ASSOC);
} else $flag = false;

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
        <li><a href="shop.php">商品檔案</a></li>
        <li class="active"><a href="leftovers_page.php">我的即期品</a></li>
        <li><a href="search_page.php">搜尋</a></li>
        </ul>
        <div class="tab-content">
            <div id="menu1" class="tab-pane fade in active">
                <h3 class="glow_light">店內即期品清單</h3>
                <!--  -->
                <br>
                <form action="leftovers_search.php">
                    <div class="form-group">
                        <label class="control-label " for="m_name">搜尋商品</label>
                        <input type="text" class="form-control input" id="m_name" placeholder="輸入欲搜尋的商品名稱" name="m_name">
                        <button type="submit" class="p btn btn-default">變更</button>
                    </div>
                </form>
                <!--  -->
                <div class="row" style="margin-left: 1px; margin-right: 1px">
                <div class="col">
                <table class="table" style=" margin-top: 15px;">
                    <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col" class="col-xs-4">餐點名稱</th>
                        <th scope="col">價格</th>
                        <th scope="col">數量</th>
                    </tr>
                    </thead>
                    <tbody>
                    <?php for ($i = 0; $i < count($meal_info); $i++): ?>
                    <tr>
                        <?php $str = str_replace(" ", "_", $meal_info[$i]['m_name']); ?>
                        <th scope="row"><?php echo $i + 1; ?></th>
                        <td><?php echo $meal_info[$i]['m_name']; ?></td>
                        <td><?php echo $meal_info[$i]['m_price']; ?></td>
                        <td>
                            <div class="row">
                                <button type="button" class="col-sm-1 change_number p btn" id="<?php echo $str."-"; ?>">-</button>
                                <p id="<?php echo $str; ?>" class="col-sm-2"><?php echo $meal_info[$i]['m_quantity']; ?></p>
                                <button type="button" class="col-sm-1 change_number p btn" id="<?php echo $str."+"; ?>">+</button>
                            </div>
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

    $(document).ready(function() {
        $('.change_number').click(function(event) {
            let m_name_with_action = event.target.id;
            let m_name = m_name_with_action.slice(0, -1);
            let action = m_name_with_action.slice(-1);
            $.ajax({
                url:'update_quantity.php',
                type: 'post',
                data: { m_name: m_name, action: action },
                success: function(response) {
                    $('#' + m_name).html(response);
                }
            });
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
            border-radius: 2px;
        }

        a {
            color: inherit;
        }

        .close {
            color: #fff; 
            opacity: 1;
        }

        p {
            text-align: center;
            padding-top: 5px;
        }
    </style>
</body>
</html>
