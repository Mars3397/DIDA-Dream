<?php
    include 'connect.php';

    if (isset($_POST["s_id"])) {
        $s_id = $_POST['s_id'];
        $stmt = $conn->prepare("select * from MylinebotApp_meals where s_id = :s_id");
        $stmt->execute(array('s_id' => $s_id));
        $meals = $stmt->fetchAll(PDO::FETCH_ASSOC);
        
        $output = '<div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title glow_light">即期品清單</h4>
        </div>
        <div class="row-xs-8 modal-body">
            <div>
            <table class="table" style=" margin-top: 15px;">
                <thead>
                <tr>
                    <th scope="col">商品名稱</th>
                    <th scope="col">數量</th>
                </tr>
                </thead>
                <tbody>';
        for ($j = 0; $j < count($meals); $j++): 
            $next_j = $j + 1;
            $output .= '<tr style="height: 45px;">
            <td>'.$meals[$j]["m_name"].'</td>
            <td>'.$meals[$j]["m_quantity"].'</td>
            </tr>';
        endfor;
        $output .= '</tbody>
                </table>
                </div>
            </div>';

        echo $output;
    }
?>
