<?php
include 'connect.php';

$stmt = $conn->prepare("select * from MylinebotApp_shops where s_id = :s_id");
$stmt->execute(array('s_id' => $_SESSION['s_id']));
$shop_info = $stmt->fetch();

try {
    if ($_POST['new_name'] == "") {
        $new_name = $shop_info['s_name'];
    } else {
        $new_name = $_POST['new_name'];
    }
    if ($_POST['new_type'] == "") {
        $new_type = $shop_info['s_type'];
    } else {
        $new_type = $_POST['new_type'];
    }
    if ($_POST['new_address'] == "") {
        $new_address = $shop_info['s_address'];
        $new_longitude = $shop_info['s_longtitude'];
        $new_latitude = $shop_info['s_latitude'];
    } else {
        $new_address = $_POST['new_address'];
        $new_longitude = $_POST['lon'];
        $new_latitude = $_POST['lat'];
    }
    $s_id = $_SESSION['s_id'];

    $stmt = $conn->prepare("update MylinebotApp_shops set s_longtitude = :s_longtitude, s_latitude = :s_latitude 
            , s_name = :s_name, s_category = :s_category, s_address = :s_address where s_id = :s_id");
    $stmt->execute(array('s_longtitude' => $new_longitude, 's_latitude' => $new_latitude, 
        's_id' => $s_id, 's_name' => $new_name, 's_category' => $new_type, 's_address' => $new_address));
    
    echo <<< EOT
    <!DOCTYPE html>
    <html> 
        <body>
            <script>
                alert("更改成功");
                window.location.replace('edit_user.php');
            </script
        </body> 
    </html> 
    EOT;
    exit();
}
catch(Exception $e) {
    $msg = $e->getMessage();
    # pop up the error message
    echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body> 
                    <script>
                        alert("$msg");
                        window.location.replace('shop.php');
                    </script>
                </body> 
            </html> 
        EOT;
}
?>