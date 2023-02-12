<?php
include 'connect.php';

// $shop_name = $_SESSION['s_name'];
$s_id = $_SESSION['s_id'];
$stmt = $conn->prepare("select * from MylinebotApp_meals where id = :id and s_id = :s_id");
$stmt->execute(array('id' => $_POST['id'], 's_id' => $s_id));
$info = $stmt->fetch();

try {

    if (empty($_POST['new_price'])) {
        throw new Exception('Please input at least one column');
    }

    # assign variables
    $new_price = $_POST['new_price'];

    $stmt = $conn->prepare("update MylinebotApp_meals set m_price = :m_price where id = :id and s_id = :s_id");
    $stmt->execute(array('m_price' => $new_price, 'id' => $_POST['id'], 's_id' => $s_id));
    
    echo <<< EOT
    <!DOCTYPE html>
    <html> 
        <body>
            <script>
                alert('編輯成功 !!');
                window.location.replace('shop.php');
            </script>
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