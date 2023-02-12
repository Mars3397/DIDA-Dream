<?php

session_start();
$dbservername = 'localhost';
$dbname = 'mysql';
$dbusername = 'DIDA-Dream';
$dbpassword = 'didadida15w';

$conn = new PDO ("mysql:host=$dbservername;dbname=$dbname", $dbusername, $dbpassword);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

?>
