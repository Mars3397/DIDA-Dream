<?php
include 'connect.php';
$u_id = $_SESSION['u_id'];
$s_id = $_SESSION['s_id'];

try {
    # check there is an input
    if ( $_POST['input'] == "" ) {
        $_SESSION['search'] = NULL;
    } else {
        # assign variables
        $m_name = $_POST['input'];

        # get user's current position
        $stmt = $conn->prepare("select * from MylinebotApp_meals where s_id = :s_id and m_name like :m_name");
        $stmt->execute(array('s_id' => $s_id, 'm_name' => '%'.$m_name.'%'));
        $meal_info = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $_SESSION['search'] = $meal_info;
    }
    echo <<< EOT
        <!DOCTYPE html>
        <html> 
            <body> 
                <script>
                    window.location.replace('shop.php');
                </script>
            </body> 
        </html> 
    EOT;
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