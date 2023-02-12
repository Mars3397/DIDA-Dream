<?php
	include '../connect.php';
	$u_id = $_SESSION['u_id'];
	
	# fetch user info
	$stmt = $conn->prepare("select * from MylinebotApp_users where u_id = :u_id");
	$stmt->execute(array('u_id' => $u_id));
	$info = $stmt->fetch();
?>


<!DOCTYPE html>
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>You Are What You Eat 測驗</title>

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
	
	<link rel="stylesheet" href="../css/bootstrap.min.css">
	<link rel="stylesheet" href="../css/animate.css">
	<link rel="stylesheet" href="../css/style.css">
	<script src="../js/modernizr-2.6.2.min.js"></script>

	</head>
	<body class="bg">
		<div class="col-md-4 col-md-offset-4">
			
			<!-- Content -->
			<div class="cent" width="100%">
			<?php if ($info['u_result'] == '青椒') : ?>
				<img src="result0.JPG" width="80%" height="auto" style="margin-top: 25px;">
			<?php elseif ($info['u_result'] == '奇異果') : ?>
				<img src="result1.JPG" width="80%" height="auto" style="margin-top: 25px;">
			<?php else : ?>
				<img src="result2.JPG" width="80%" height="auto" style="margin-top: 25px;">
			<?php endif;?>
			</div>
			
			<?php if ($info['u_result'] == '青椒') : ?>
				<img src="share0.JPG" alt="Record" id="record" hidden>
			<?php elseif ($info['u_result'] == '奇異果') : ?>
				<img src="share1.JPG" alt="Record" id="record" hidden>
			<?php else : ?>
				<img src="share2.JPG" alt="Record" id="record" hidden>
			<?php endif;?>

			<div class="cent" style="margin-top: 20px;" width="100%">
				<button id="share" style="color: black; font-size: 35px; background-color: white; border-radius: 20px; padding: 20px;" class="btn"></button>
			</div>

		</div>
		<div class="row" style="padding-top: 60px; clear: both;">
		</div>
	
	<!-- jQuery -->
	<script src="../js/jquery.min.js"></script>
	<!-- Bootstrap -->
	<script src="../js/bootstrap.min.js"></script>
	<!-- Placeholder -->
	<script src="../js/jquery.placeholder.min.js"></script>
	<!-- Waypoints -->
	<script src="../js/jquery.waypoints.min.js"></script>
	<!-- Main JS -->
	<script src="../js/main.js"></script>

	<script>
		const button = document.querySelector('#share');
		const img =  document.querySelector('#record');

		// Feature detection
		const supported = 'canShare' in navigator;
		// Update the button action text
		button.textContent = supported ? 'Share Result' : 'Download Result';

		const shareOrDownload = async (blob, fileName, title, text, url) => {
		// Using the Web Share API
		if (supported) {
			const data = {
			files: [
				new File([blob], fileName, {
				type: blob.type,
				}),
			],
			title,
			text,
			url
			};
			if (navigator.canShare(data)) {
			try {
				await navigator.share(data);
			} catch (err) {
				if (err.name !== 'AbortError') {
				console.error(err.name, err.message);
				}
			} finally {
				return;
			}
			}
		}
		// Fallback implementation.
		const a = document.createElement('a');
		a.download = fileName;
		a.style.display = 'none';
		a.href = URL.createObjectURL(blob);
		a.addEventListener('click', () => {
			setTimeout(() => {
			URL.revokeObjectURL(a.href);
			a.remove();
			}, 1000)
		});
		document.body.append(a);
		a.click();
		};

		button.addEventListener('click', async () => {
		const blob = await fetch(img.src).then(res => res.blob());
		await shareOrDownload(blob, 'myResult.png', 'DIDA Collection', '想知道你的食物人格嗎？來測驗看看吧！！', 'https://liff.line.me/1645278921-kWRPP32q/?accountId=195dceee');
		});
	</script>

    <style>
		h2 {
			line-height: 2;
		}

        .cent {
            display: flex;  
            justify-content: center;  
            align-items: center;  
        }

        .bg {
            background-color: #e8e1d2;
        }
    </style>

	</body>
</html>

