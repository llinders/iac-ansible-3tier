<?php
	require_once 'conn.php';
	error_reporting(E_ALL);
	if(ISSET($_POST['add'])){
		if($_POST['task'] != ""){
			$task = $_POST['task'];
			
			$conn->query($conn, "INSERT INTO `Task` VALUES('', '$task')");
			header('Location: index.php');
		}
	}
?>