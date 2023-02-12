<?php 
    include 'connect.php';
    $flag =  $_GET["flag"];
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
<script src="https://static.line-scdn.net/liff/edge/2/sdk.js"></script>
<script>
    $(document).ready(function() {
        const str = window.location.href;
        const destination = str.split("=")[1].split("#")[0];
        const liffId_r = "1657635549-J0klqVGR";
        const liffId_rs = "1657635549-N79kd2nl";
        const liffId_eu = "1657635549-yM4MZE73";
        const liffId_em = "1657635549-3Qg9zW6M";
        const liffId_s = "1657635549-OWpaWBKL";
        var liffId = "";
        if (destination == "eu") {
            liffId = liffId_eu;
        } else if (destination == "r") {
            liffId = liffId_r;
        } else if (destination == "rs") {
            liffId = liffId_rs;
        } else if (destination == "s") {
            liffId = liffId_s;
        } else if (destination == "em") {
            liffId = liffId_em;
        }
        liff.init({ 
            liffId
        }).then(() => {
            liff.getProfile().then((profile) => {
                const u_id = profile.userId;
                const u_name = profile.displayName;
                $.ajax({
                    url:'set_uid.php',
                    type: 'post',
                    data: { u_id: u_id, u_name: u_name }, 
                    success: function(){
                        if (destination == "eu") {
                            window.location.replace("edit_user.php");
                        } else if (destination == "r") {
                            window.location.replace("register_page.php");
                        } else if (destination == "rs") {
                            window.location.replace("register_shop.html");
                        } else if (destination == "s") {
                            window.location.replace("search_page.php");
                        } else if (destination == "em") {
                            window.location.replace("shop.php");
                        }
                    }
                });
            }).catch((err) => {
                alert(err.code, err.message);
            });
        }).catch((err) => {
            alert(err.code, err.message);
        });
    });
</script>
</body>


</html>
