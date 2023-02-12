<?php

include 'connect.php';

try {
    $u_id = $_SESSION['u_id'];

    if ($_POST['use_address'] == "keyin") {
        $u_latitude = $_POST['lat']; 
        $u_longtitude = $_POST['lon']; 
        $u_address = $_POST['address'];
    } else {
        $u_longtitude = 121.5751213; 
        $u_latitude = 25.0770622;
        $u_address = "台北市內湖區瑞光路333號";
    }
    $u_role = "u";
    $u_give = 0;
    $s_category = $_POST['s_category'];
    $m_group = $_POST['m_group'];
    $f_time = $_POST['f_time'];
    if ($_POST['u_name']) {
        $u_name = $_POST['u_name'];
    } else {
        $u_name = $_SESSION['u_name'];
    }

    $stmt = $conn->prepare("update MylinebotApp_users set u_latitude = :u_latitude , u_longtitude = :u_longtitude,
                            u_role = :u_role, u_give = :u_give, u_name = :u_name, u_address = :u_address where u_id = :u_id");
    // $stmt = $conn->prepare("update MylinebotApp_users (u_id, u_latitude, u_longtitude, u_role, u_give, u_name, u_address) 
    //                         values (:u_id, :u_latitude, :u_longtitude, :u_role, :u_give, :u_name, :u_address);");
    $stmt->execute(array('u_latitude' => $u_latitude, 'u_longtitude' => $u_longtitude,
                'u_role' => $u_role, 'u_give' => $u_give, 'u_name' => $u_name, 'u_id' => $u_id, 'u_address' => $u_address));

    $stmt = $conn->prepare("delete from MylinebotApp_favor_shop where u_id = :u_id");
    $stmt->execute(array('u_id' => $u_id));
    $stmt = $conn->prepare("delete from MylinebotApp_favor_food where u_id = :u_id");
    $stmt->execute(array('u_id' => $u_id));
    $stmt = $conn->prepare("delete from MylinebotApp_favor_time where u_id = :u_id");
    $stmt->execute(array('u_id' => $u_id));

    for($i = 0; $i < count($s_category); $i++){
        $s_c = $s_category[$i];
        $stmt1 = $conn->prepare("insert into MylinebotApp_favor_shop (u_id, s_category) 
                    values (:u_id, :s_c);");
        $stmt1->execute(array('u_id' => $u_id, 's_c' => $s_c));
    }

    for($i = 0; $i < count($m_group); $i++){
        $m_g = $m_group[$i];
        $stmt2 = $conn->prepare("insert into MylinebotApp_favor_food (u_id, m_group) 
            values (:u_id, :m_g);");
        $stmt2->execute(array('u_id' => $u_id, 'm_g' => $m_g));
    }

    for($i = 0; $i < count($f_time); $i++){
        $f_t = $f_time[$i];
        $stmt3 = $conn->prepare("insert into MylinebotApp_favor_time (u_id, f_time) 
            values (:u_id, :f_t);");
        $stmt3->execute(array('u_id' => $u_id, 'f_t' => $f_t));
    }

    echo <<< EOT
        <!DOCTYPE html>
        <html> 
            <body>
                <script>
                    alert("更改成功！");
                    window.location.replace('edit_user.php');
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
                        window.location.replace('edit_user.php');
                    </script>
                </body> 
            </html> 
        EOT;
}

?>


