<?php

include 'connect.php';

try {
    # check for empty columns
    if ($_POST['s_name']=="" ||
        $_POST['s_category']=="") {
        throw new Exception('請輸入所有欄位！');
    }
    
    # assign variables
    $s_name = $_POST['s_name'];
    $u_id = $_SESSION['u_id'];
    $s_latitude = $_POST['lat'];
    $s_longitude = $_POST['lon'];
    $s_category = $_POST['s_category'];
    $s_address = $_POST['address'];

    $s_openday = '';
    if ($_POST['s_openday1'] != "") {
        $s_openday .= '1';
    } else {
        $s_openday .= '0';
    }
    if ($_POST['s_openday2'] != "") {
        $s_openday .= '1';
    } else {
        $s_openday .= '0';
    }
    if ($_POST['s_openday3'] != "") {
        $s_openday .= '1';
    } else {
        $s_openday .= '0';
    }
    if ($_POST['s_openday4'] != "") {
        $s_openday .= '1';
    } else {
        $s_openday .= '0';
    }
    if ($_POST['s_openday5'] != "") {
        $s_openday .= '1';
    } else {
        $s_openday .= '0';
    }
    if ($_POST['s_openday6'] != "") {
        $s_openday .= '1';
    } else {
        $s_openday .= '0';
    }
    if ($_POST['s_openday7'] != "") {
        $s_openday .= '1';
    } else {
        $s_openday .= '0';
    }

    $s_start_time = $_POST['start'];
    $s_end_time = $_POST['end'];
    $s_level = "0";
    $s_city = "台中";

    $stmt = $conn->prepare("update MylinebotApp_users set u_role = :u_role where u_id = :u_id");
    $stmt->execute(array('u_role' => 's', 'u_id' => $u_id));

    $stmt = $conn->prepare("insert into MylinebotApp_shops (s_name, u_id, s_category, s_latitude, s_longtitude, s_address, 
                    s_openday, s_start_time, s_end_time, s_level, s_city) 
                    values (:s_name, :u_id, :s_category, :s_latitude, :s_longtitude, :s_address, :s_openday, :s_start_time, :s_end_time, :s_level, :s_city);");
    $stmt->execute(array('s_name' => $s_name, 'u_id' => $u_id, 's_category' => $s_category, 's_latitude' => $s_latitude,
                    's_longtitude' => $s_longitude, 's_address' => $s_address, 's_openday' => $s_openday, 
                    's_start_time' => $s_start_time, 's_end_time' => $s_end_time, 's_level' => $s_level, 's_city' => $s_city));

    # pop up the message
    echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        alert("註冊成功");
                        window.location.replace('shop.php');
                    </script>
                </body> 
            </html> 
        EOT;
    exit();
} 
# catch the exceptions
catch(Exception $e) {
    $msg = $e->getMessage();
    session_unset();
    session_destroy();
    # pop up the error message
    echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body> 
                    <script>
                        alert("$msg");
                        window.location.replace('register_shop.html');
                    </script>
                </body> 
            </html> 
        EOT;
}

?>


