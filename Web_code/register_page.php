<?php
	include 'connect.php';
	# fetch user info
	$stmt = $conn->prepare("select * from MylinebotApp_users where u_id = :u_id");
	$stmt->execute(array('u_id' => $_SESSION['u_id']));
	$info = $stmt->fetch();
?>

<!DOCTYPE html>
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>填寫個人資料</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Free HTML5 Template by FreeHTML5.co" />
	<meta name="keywords" content="free html5, free template, free bootstrap, html5, css3, mobile first, responsive" />
	<meta name="author" content="FreeHTML5.co" />

  	<!-- Facebook and Twitter integration -->
	<meta property="og:title" content=""/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content=""/>
	<meta property="og:description" content=""/>
	<meta name="twitter:title" content="" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />

	<!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
	<link rel="shortcut icon" href="favicon.ico">

	<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700,300' rel='stylesheet' type='text/css'>
	
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<link rel="stylesheet" href="css/animate.css">
	<link rel="stylesheet" href="css/style.css">

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>

	<!-- Modernizr JS -->
	<script src="js/modernizr-2.6.2.min.js"></script>

	</head>
	<body>
	
		<div class="container glow">
		
			<div class="row">
				<div class="col-md-4 col-md-offset-4">
					<!-- Start Sign In Form -->
					<form action="register.php" class="fh5co-form animate-box bg" data-animate-effect="fadeIn" method="post" id="myform">
						<h2 style="color: #fffae3;" class="glow_light">填寫個人資料</h2>
						<input type="hidden" value="<?php echo $info['u_name']; ?>" name="u_name">
						<div class="form-group">
							<label style="font-weight: bold;">想收到哪裡的即期品資訊：</label><br>
							<div>
								<input type="radio" name="use_address" value="now" id="now"/>
								<label for="now" style="margin-right: 5px;">直接使用現在位置 </label>
							</div>
							<div>
								<input type="radio" name="use_address" value="keyin" id="keyin"/>
								<label for="keyin" style="margin-right: 5px;">手動輸入（請填寫下方欄位） </label>
							</div>
							<input type="text" style="border-bottom: 1px solid #fffae3; color: white;" class="input" id="address" autocomplete="off" name="address" placeholder="以地標或地址填寫">
							<input type="hidden" id="lat" name="lat" value="a">
							<input type="hidden" id="lon" name="lon" value="b">
						</div>

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

						<div class="form-group">
							<input type="checkbox" id="read" required>
							<label for="read">我已完成閱讀並同意<a href="privacy_doc.html">隱私權條款說明文件</a></label>
						</div>

						<div class="form-group">
							<input type="submit" value="註冊" class="p btn btn-light" id="sb_btn" disabled>
						</div>
						
					</form>
					<!-- END Sign In Form -->

				</div>
			</div>
		</div>
	
	<!-- jQuery -->
	<script src="js/jquery.min.js"></script>
	<!-- Bootstrap -->
	<script src="js/bootstrap.min.js"></script>
	<!-- Placeholder -->
	<script src="js/jquery.placeholder.min.js"></script>
	<!-- Waypoints -->
	<script src="js/jquery.waypoints.min.js"></script>
	<!-- Main JS -->
	<script src="js/main.js"></script>

	<script
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBKaRPTrJub0mPX86F8q_DBSpV8zQs56xM"
      defer
    ></script>

	<script src="https://static.line-scdn.net/liff/edge/2/sdk.js"></script>

	<script>
		$(document).ready(function() {
			$("#address").on('input', function() {
				var address = document.getElementById('address').value;

				if (address != '') {
					var geocoder = new google.maps.Geocoder();
					geocoder.geocode( { 'address': address }, function(results, status) {
						if (status == 'OK') {
							document.getElementById('lat').value = results[0].geometry.location.lat();
							document.getElementById('lon').value = results[0].geometry.location.lng();
						}
					});
				}
			});
		});

		$(document).ready(function() {
			$("#read").on('click', function() {
				var event_object = document.getElementById('read');
				if (event_object.checked) {
					document.getElementById('sb_btn').removeAttribute("disabled");
				} else {
					document.getElementById('sb_btn').disabled = true;
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

        .p {
            font-family: Garamond, serif;
            background-color: #d4d4d4;
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
            border: none;
            border-bottom: 1px solid #fffae3;
            border-radius: 2px;
        }

		.input::placeholder {
			/* color: #fffaf3; */
		}
    </style>

	</body>
</html>

