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
            border: none;
            border-bottom: 1px solid #fffae3;
            border-radius: 2px;
        }

		::placeholder {
			color: white;
		}
    </style>

	<!-- Modernizr JS -->
	<script src="js/modernizr-2.6.2.min.js"></script>

	</head>
	<body>
	
		<div class="container glow">
		
			<div class="row">
				<div class="col-md-4 col-md-offset-4">
					<!-- Start Sign In Form -->
					<div class="fh5co-form animate-box bg" data-animate-effect="fadeIn">
						<h2 style="color: #fffae3;" class="glow_light">選擇身份</h2>
                        <div class="row" style="margin-left: 10px;">
                            <button id="u" class="in p btn">一般使用者</button>
                            <button id="s" class="in p btn" style="margin-left: 40%;">商家</button>
                        </div>
                    </div>
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

    <script>
        $(document).ready(function() {
            $('.in').click(function(event) {
                var u_role = event.target.id;
                $.ajax({
                    url:'register1.php',
                    type: 'post',
                    data: { u_role: u_role },
                    success: function(response) {
                        window.location.replace(response);
                    }
                });
            });
        });
    </script>

	</body>
</html>