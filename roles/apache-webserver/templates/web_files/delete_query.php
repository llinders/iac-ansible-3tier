<?php
	require_once 'conn.php';
	
	if($_GET['task_id']){
		$task_id = $_GET['task_id'];
		
		$pg_query($conn, "DELETE FROM `task` WHERE `id` = $task_id");
		header("location: index.php");
	}	
?>