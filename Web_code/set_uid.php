<?php
    include 'connect.php';
    $u_id = $_POST['u_id'];
    $_SESSION['u_id'] = $u_id;
    $_SESSION['u_name'] = $_POST['u_name'];

    $stmt = $conn->prepare("select u_role from MylinebotApp_users where u_id = :u_id");
    $stmt->execute(array('u_id' => $u_id));
    $info = $stmt->fetch()[0];
    $_SESSION['u_role'] = $info;
?>