<?php

include 'connect.php';

# assign variables
$u_id = $_SESSION['u_id'];
$u_role = $_POST['u_role'];
$_SESSION['u_role'] = $u_role;

if ($u_role == 's'){
    echo 'register_shop.html';
}
else {
    echo 'register_page.php';
}

?>


