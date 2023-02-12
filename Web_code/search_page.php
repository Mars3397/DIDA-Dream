<?php 
include 'connect.php';
$u_account = $_SESSION['u_account'];
$search_info = $_SESSION['search_info'];
$input_data = $_SESSION['input_data'];

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
      border-radius: 2px;
    }

    .input {
      color: #a4a4a4;
      background: #120f28;
      border: none;
      border-bottom: 1px solid #fffae3;
      border-radius: 2px;
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

    select {
      color: #d4d4d4;
    }

    .close {
      color: #fff; 
      opacity: 1;
    }
  </style>
</head>

<body>
  <div class="container glow" style="margin-top: 10px;">

    <ul class="nav nav-tabs">
        <li><a href="edit_user.php">資料</a></li>
        <?php if ($_SESSION['u_role'] == 's') : ?>
          <li><a href="shop.php">商品檔案</a></li>
          <li><a href="leftovers_page.php">我的即期品</a></li>
        <?php endif;?>
        <li  class="active"><a href="search_page.php">搜尋</a></li>
    </ul>
        <h3 class="glow_light">搜尋即期品</h3><br>
        <div class="row col-xs-10">
          <form class="form-horizontal" action="search.php" method="post">

            <div class="form-group">
              <label class="control-label col-sm-2" for="Shop">店家名稱</label>
              <div class="col-sm-5">
                <input type="text" class="form-control" placeholder="請輸入店家名稱" name="shop">
                <!-- <p class="input">請輸入店家名稱</p> -->
              </div>
            </div>

            <div class="form-group">
            <label class="control-label col-sm-2" for="Meal">餐點品項</label>
              <div class="col-sm-5">
                <select class="form-control" id="Meal" name="meal">
                  <option></option>
                  <option>飯糰手卷</option>
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

            <div class="form-group">
              <label class="control-label col-sm-2" for="category">店家分類</label>
              <div class="col-sm-5">
                <select class="form-control" id="category" name="s_category">  
                  <option></option>
                  <option>7-11</option>
                  <option>全家</option>
                  <option>麵包店</option>
                </select>
              </div>
            </div>

            <div class="form-group">
            <label class="control-label col-sm-2" for="sort">排序</label>
              <div class="col-sm-3" style="margin-top: 5px;">
                <select class="form-control" id="sort" name="sort">
                  <option>Shop Name</option>
                  <option>Category</option>
                </select>
              </div>
              <div class="col-sm-3" style="margin-top: 5px;">
                <select class="form-control" id="sort2" name="sort2">
                  <option>Ascending</option>
                  <option>Descending</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <br>
              <button type="submit" style="margin-left: 18px;" class="p btn">搜尋</button>
            </div>

          </form>
        </div>

        <!-- ----------------------------------------------------------------------- -->
        <div class="row" style="margin-left: 1px; margin-right: 1px">
          <?php
              $data_nums = count($search_info); 
              $per = 20;
              $pages = ceil($data_nums / $per);
              if (!isset($_GET["page"])) $page = 1;
              else $page = intval($_GET["page"]);

              $start = ($page - 1) * $per;
              $stmt = $conn->prepare($_SESSION['search_sql'].' limit '.$start.', '.$per);
              $stmt->execute($_SESSION['sql_data']);
              $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
          ?>
          <table class="table" style=" margin-top: 15px;">
            <thead>
              <tr>
                <!-- <th scope="col">#</th> -->
                <th scope="col">店家名稱</th>
                <th scope="col">店家分類</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <?php for ($i = 0; $i < count($result); $i++): ?>
                <tr>
                  <!-- <th scope="row"><?php echo $i + $start + 1; ?></th> -->
                  <td><?php echo $result[$i]['s_name']; ?></td>
                  <td><?php echo $result[$i]['s_category']; ?></td>
                  <!-- <td> <button type="button" class="btn btn-info " data-toggle="modal" data-target="#colapse">Open Menu</button></td> -->
                  <td> <input type="button" class="p btn open_menu" data-toggle="modal" data-target="#colapse" name="open" value="看更多" id="<?php echo $result[$i]['id'];?>" > </td>
                </tr>
              <?php endfor; ?>
            </tbody>
          </table>
          <br>
          <?php
            if ($page + 1 <= $pages) $next_page = $page + 1;
            else $next_page = $page;

            if ($page - 1 > 0) $pre_page = $page - 1;
            else $pre_page = $page;

            echo "<a href=?page=".$pre_page.">上ㄧ頁 </a> ";
            echo " 第 ";
            if ($pages > 10) {
              for ($j = 1; $j <= 5; $j++) :
                echo " <a href=?page=".$j."> ".$j." </a> ";
              endfor;
              echo "   ...   ";
              for ($j = $pages-5; $j <= $pages; $j++) :
                echo " <a href=?page=".$j."> ".$j." </a> ";
              endfor;
            } else {
              for ($j = 1; $j <= $pages; $j++) :
                echo " <a href=?page=".$j."> ".$j." </a> ";
              endfor;
            }
            echo " 頁 <a href=?page=".$next_page."> 下一頁</a> <br> <br>";
          ?>

          <!-- Modal -->
          <div class="modal fade black" id="colapse" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
              <!-- Modal content-->
              <div class="modal-content glow bg">
                <div id="menu-detail">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Option 1: Bootstrap Bundle with Popper -->
  <!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script> -->
  <script>
    $(document).ready(function () {
      $(".nav-tabs a").click(function () {
        $(this).tab('show');
      });
    });
  </script>

  <script>
    $(document).ready(function(){
      $('.open_menu').click(function(){
        var s_id = $(this).attr("id");
        $.ajax({
          url: "select.php",
          method: "post",
          data: { s_id: s_id },
          success: function(data){
            $('#menu-detail').html(data);
            $('#colapse').modal("show");
          }
        })
      })
    });
  </script>
</body>
</html>