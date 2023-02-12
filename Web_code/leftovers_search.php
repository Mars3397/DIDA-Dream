<?php
include 'connect.php';
$u_id = $_SESSION['u_id'];
$s_id = $_SESSION['s_id'];

try {
    
    # check there is an input
    if ( $_POST['input'] == "" ) {
        throw new Exception('請輸入欲搜尋之商品名稱 !!');
    }

    # assign variables
    $m_name = $_POST['input'];

    # get user's current position
    $stmt = $conn->prepare("select * from MylinebotApp_meals where s_id = :s_id and m_name like :m_name");
    $stmt->execute(array('s_id' => $s_id, 'm_name' => '%'.$m_name.'%'));
    $meal_info = $stmt->fetchAll(PDO::FETCH_ASSOC);

    $output='<div class="row" style="margin-left: 1px; margin-right: 1px">
        <div class="col">
            <table class="table" style=" margin-top: 15px;">
                <thead>
                <tr>
                    <th scope="col">
                    <th scope="col" class="col-xs-4">餐點名稱</th>
                    <th scope="col">價格</th>
                    <th scope="col">數量</th>
                </tr>
                </thead>
                <tbody>';

    for ($i = 0; $i < count($meal_info); $i++):
        $str = str_replace(" ", "_", $meal_info[$i]['m_name']);
        $output .= '<tr>'.
            '<th scope="row">'.($i + 1).'</th>
            <td>'.$meal_info[$i]['m_name'].'</td>
            <td>'.$meal_info[$i]['m_price'].'</td>
            <td>
                <div class="row">
                    <button type="button" class="col-sm-2 model_change_number p btn" id="model'.$str.'-">-</button>
                    <p id="model'.$str.'" class="col-sm-2">'.$meal_info[$i]['m_quantity'].'</p>
                    <button type="button" class="col-sm-2 model_change_number p btn" id="model'.$str.'+">+</button>
                </div>
            </td>
        </tr>';
    endfor;
    $output .= '</tbody>
            </table>
        </div>
    </div>';
    echo $output;
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
                        window.location.replace('leftovers_page.php');
                    </script>
                </body> 
            </html> 
        EOT;
}
?>