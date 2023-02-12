<?php
include 'connect.php';

$s_id = $_SESSION['s_id'];
$m_name = $_POST['m_name'];
$action = $_POST['action'];

$stmt = $conn->prepare("select m_quantity from MylinebotApp_meals where m_name = :m_name and s_id = :s_id");
$stmt->execute(array('m_name' => $m_name, 's_id' => $s_id));
$m_quantity = $stmt->fetch()[0];


if ($action == "+") {
    $stmt = $conn->prepare("update MylinebotApp_meals set m_quantity = :m_quantity where m_name = :m_name and s_id = :s_id");
    $stmt->execute(array('m_quantity' => $m_quantity + 1, 'm_name' => $m_name, 's_id' => $s_id));
    echo $m_quantity + 1;
} else {
    if ($m_quantity > 0) {
        $stmt = $conn->prepare("update MylinebotApp_meals set m_quantity = :m_quantity where m_name = :m_name and s_id = :s_id");
        $stmt->execute(array('m_quantity' => $m_quantity - 1, 'm_name' => $m_name, 's_id' => $s_id));
        echo $m_quantity - 1;
    } else {
        echo $m_quantity;
    }
}

// exit();
?>