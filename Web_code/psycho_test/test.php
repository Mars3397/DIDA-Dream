<?php
    include '../connect.php';

    $q = $_POST['q'];
    $u_id = $_SESSION['u_id'];
    
    if ($q == "start") {
        echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        window.location.replace('test_page4.php');
                    </script>
                </body> 
            </html> 
        EOT;
    } 
    if ($q == 1) {
        echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        window.location.replace('test_page2.php');
                    </script>
                </body> 
            </html> 
        EOT;
    } 
    if ($q == 2) {
        $stmt = $conn->prepare("update MylinebotApp_users set u_type = :u_type where u_id = :u_id");
        $stmt->execute(array('u_type' => $_POST['a5'], 'u_id' => $u_id));
        echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        window.location.replace('test_page3.php');
                    </script>
                </body> 
            </html> 
        EOT;
    } 
    if ($q == 3) {
        if ($_POST['a1']) {
            $result = $_POST['a1'];
        } 
        if ($_POST['a2']) {
            $result = $_POST['a2'];
        }
        if ($_POST['a3']) {
            $result = $_POST['a3'];
        }
        $stmt = $conn->prepare("update MylinebotApp_users set u_result = :u_result where u_id = :u_id");
        $stmt->execute(array('u_result' => $result, 'u_id' => $u_id));
        echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        window.location.replace('test_page4.php');
                    </script>
                </body> 
            </html> 
        EOT;
    } 
    if ($q == 4) {
        echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        window.location.replace('test_page5.php');
                    </script>
                </body> 
            </html> 
        EOT;
    } 
    if ($q == 5) {
        if ($_POST['a1']) {
            $result = $_POST['a1'];
        } 
        if ($_POST['a2']) {
            $result = $_POST['a2'];
        }
        if ($_POST['a3']) {
            $result = $_POST['a3'];
        }
        $stmt = $conn->prepare("update MylinebotApp_users set u_result = :u_result where u_id = :u_id");
        $stmt->execute(array('u_result' => $result, 'u_id' => $u_id));
        echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        window.location.replace('test_page6.php');
                    </script>
                </body> 
            </html> 
        EOT;
    } 
    if ($q == 6) {
        if ($_POST['a1']) {
            $type = $_POST['a1'];
        } 
        if ($_POST['a2']) {
            $type = $_POST['a2'];
        }
        if ($_POST['a3']) {
            $type = $_POST['a3'];
        }
        $stmt = $conn->prepare("update MylinebotApp_users set u_type = :u_type where u_id = :u_id");
        $stmt->execute(array('u_type' => $type, 'u_id' => $u_id));
        echo <<< EOT
            <!DOCTYPE html>
            <html> 
                <body>
                    <script>
                        window.location.replace('final.php');
                    </script>
                </body> 
            </html> 
        EOT;
    } 
    
?>