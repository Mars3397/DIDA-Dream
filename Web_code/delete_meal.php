<?php
include 'connect.php';
// $shop_name = $_SESSION['s_name'];
$s_id = $_SESSION['s_id'];

if(isset($_POST['delete'])) {
    $stmt = $conn->prepare("delete from MylinebotApp_meals where binary id = :id and s_id = :s_id");
    $stmt->execute(array('id' => $_POST['id'], 's_id' => $s_id));
}
echo <<< EOT
    <!DOCTYPE html>
    <html> 
        <body>
            <script>
                alert('刪除成功 !!');
                window.location.replace('shop.php');
            </script>
        </body> 
    </html> 
EOT;
exit();
?>