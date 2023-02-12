<?php
include 'connect.php';
$u_id = $_SESSION['u_id'];

try {
    # assign variables
    $shop = $_POST['shop'];
    $m_group = $_POST['meal'];
    $s_category = $_POST['s_category'];
    $sort = $_POST['sort'];
    $sort2 = $_POST['sort2'];
    $_SESSION['input_data'] = array($shop, $distance, $m_group, $s_category, $sort, $sort2);

    # get user's current position
    $stmt = $conn->prepare("select * from MylinebotApp_users where u_id = :u_id");
    $stmt->execute(array('u_id' => $u_id));
    $user_info = $stmt->fetch();
    $u_longitude = $user_info['u_longitude'];
    $u_latitude = $user_info['u_latitude'];
    $sql_data['u_longitude'] = $u_longitude;
    $sql_data['u_latitude'] = $u_latitude;

    $condition = "select distinct MylinebotApp_shops.id, MylinebotApp_shops.s_id, MylinebotApp_shops.s_name, MylinebotApp_shops.s_category, st_distance_sphere(point(:u_longitude, :u_latitude), point(MylinebotApp_shops.s_longtitude, MylinebotApp_shops.s_latitude)) as distance
         from MylinebotApp_shops left outer join MylinebotApp_meals on MylinebotApp_shops.s_id = MylinebotApp_meals.s_id where MylinebotApp_shops.s_name like '%'";
    
    if ($shop) {
        $condition = $condition . " and MylinebotApp_shops.s_name like :shop";
        $sql_data['shop'] = '%'.$shop.'%';
    }
    if ($distance != 'None') {
        if ($distance == 'Near')
            $condition = $condition . " and st_distance_sphere(point(:u_longitude, :u_latitude), point(MylinebotApp_shops.s_longtitude, MylinebotApp_shops.s_latitude)) <= 2000";
        if ($distance == 'Medium')
            $condition = $condition . " and st_distance_sphere(point(:u_longitude, :u_latitude), point(MylinebotApp_shops.s_longtitude, MylinebotApp_shops.s_latitude)) > 2000 
                and st_distance_sphere(point(:u_longitude, :u_latitude), point(MylinebotApp_shops.s_longtitude, MylinebotApp_shops.s_latitude)) <= 5000";     
        if ($distance == 'Far')
            $condition = $condition . " and st_distance_sphere(point(:u_longitude, :u_latitude), point(MylinebotApp_shops.s_longtitude, MylinebotApp_shops.s_latitude)) > 5000";
    }
    if ($m_group) {
        $condition = $condition . " and MylinebotApp_meals.m_group like :m_group";
        $sql_data['m_group'] = '%'.$m_group.'%';
    }
    if ($s_category) {
        $condition = $condition . " and MylinebotApp_shops.s_category like :s_category";
        $sql_data['s_category'] = '%'.$s_category.'%';
    }

    # Sort
    if ($sort == 'Shop Name') $condition = $condition . " order by MylinebotApp_shops.s_name";
    if ($sort == 'Category') $condition = $condition . " order by MylinebotApp_shops.s_category";
    if ($sort == 'Distance') $condition = $condition . " order by st_distance_sphere(point($u_longitude, $u_latitude), point(MylinebotApp_shops.s_longtitude, MylinebotApp_shops.s_latitude))";
    if ($sort2 == 'Descending') $condition = $condition . " desc";
    
    $stmt = $conn->prepare($condition);
    $stmt->execute($sql_data);
    $search_info = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $_SESSION['search_sql'] = $condition;
    $_SESSION['sql_data'] = $sql_data;
    $_SESSION['search_info'] = $search_info;

    echo <<< EOT
    <!DOCTYPE html>
    <html> 
        <body>
            <script>
                window.location.replace('search_page.php');
            </script>
        </body> 
    </html> 
    EOT;
    exit();
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
                        window.location.replace('search_page.php');
                    </script>
                </body> 
            </html> 
        EOT;
}
?>