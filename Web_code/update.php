<?php
include 'connect.php';

$stmt = $conn->prepare("select * from MylinebotApp_shops");
$stmt->execute(array());
$shop_info = $stmt->fetchAll(PDO::FETCH_ASSOC);

for ($i = 0; $i < count($shop_info); $i++):
    $stmt = $conn->prepare("select s_id from MylinebotApp_family_shops where s_name = :s_name");
    $stmt->execute(array('s_name' => $shop_info[$i]['s_name']));
    $id = $stmt->fetch()[0];
    $stmt = $conn->prepare("update MylinebotApp_shops set id = :id where s_name = :s_name");
    $stmt->execute(array('id' => $id, 's_name' => $shop_info[$i]['s_name']));
endfor;

echo "Done";
?>