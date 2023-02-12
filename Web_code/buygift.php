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
  <title>購買即食券</title>
  <script>
    function change(){
        document.getElementById("photo").src="src/payment.jpg";
        $('#info').modal('hide');
    }
    function show(){
        $('#info').modal('show');
    }
    </script>
    <style>
        .cent {
            display: flex;  
            justify-content: center;  
            align-items: center;  
        }
    </style>
</head>
    <body>
        <div class="container">
            <div class="cent">
                <img id="photo" src='src/gift.png' alt="buygift" width="100%" height="auto" class="center" usemap="#workmap">
                <map name="workmap">
                    <area shape="rect" coords="175,700,380,800" onclick="show()">
                </map>
            </div>

            <div class="modal fade" id="info" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true"> 
                <div class="modal-dialog modal-sm">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">捐贈須知</h4>
                        </div>
                        <div class="modal-body">
                            <p>非常感謝您加入「即食予計畫」，為保障您的權益，請您詳閱下列內容：</p>
                            
                            <br>
                            <h4>一、您的捐贈將如何被使用</h4>
                            <p>我們會於後端資料庫進行即時捐贈配對，將您的愛心捐贈給政府認證之受助者，系統也將於配對完成時通知您！</p>

                            <br>
                            <h4>二、個人資料之保護</h4>
                            <p>在愛心捐贈的過程中，捐贈者及受助者的資料都將進行嚴格保護，完整的隱私權條款請詳閱<a href="privacy_doc.html">隱私權條款說明文件</a>。</p>

                        </div>
                        <div class="modal-footer">
                            <button type="btn" class="btn btn-default" onclick="change()">我瞭解了</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
    </body>
</html>