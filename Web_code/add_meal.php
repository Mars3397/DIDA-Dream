<?php 

include 'connect.php';
$s_name = $_SESSION['s_name'];
$s_id = $_SESSION['s_id'];

try {
    # check for empty columns
    if (empty($_POST['m_name']) || empty($_POST['m_price']) || empty($_POST['m_group'])) {
        throw new Exception('Please input all the columns !!');
    }

    # assign variables
    $m_name = $_POST['m_name'];
    $m_price = $_POST['m_price'];
    $m_quantity = 0;
    $m_group = $_POST['m_group'];

    # check if the shop name is unique
    $stmt = $conn->prepare("select * from MylinebotApp_meals where s_id = :s_id and m_name = :m_name");
    $stmt->execute(array('s_id' => $s_id, 'm_name' => $m_name));
    if ($stmt->rowCount() == 0) {
        $stmt = $conn->prepare("insert into MylinebotApp_meals (m_name, s_id, m_price, m_quantity, m_group) 
                        values (:m_name, :s_id, :m_price, :m_quantity, :m_group);");
        $stmt->execute(array('m_name' => $m_name, 's_id' => $s_id, 'm_price' => $m_price, 
        'm_quantity' => $m_quantity, 'm_group' => $m_group));

        # pop up message
        echo <<< EOT
                <!DOCTYPE html>
                <html> 
                    <body>
                        <script>
                            alert("已新增餐點 !!");
                            window.location.replace('shop.php');
                        </script>
                    </body> 
                </html> 
            EOT;
        exit();
    } else 
        throw new Exception("The meal has been added !!");
}

# catch the exceptions
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