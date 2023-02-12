<?php
include 'connect.php';

// $shop_name = $_SESSION['s_name'];
$s_id = $_SESSION['s_id'];

try {

    $stmt = $conn->prepare("update MylinebotApp_meals set m_quantity = :m_quantity where s_id = :s_id");
    $stmt->execute(array('m_quantity' => 0, 's_id' => $s_id));
    
    echo <<< EOT
    <!DOCTYPE html>
    <html> 
        <body>
            <script>
                alert('清除成功 !!');
                window.location.replace('leftovers_page.php');
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
                        window.location.replace('leftovers_page.php');
                    </script>
                </body> 
            </html> 
        EOT;
}
?>