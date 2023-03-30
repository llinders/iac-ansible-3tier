<?php
	require_once 'conn.php';
	
	if($_GET['task_id']){
		$sql = 'DELETE FROM Task WHERE id = ?';
		$stmt = $conn->prepare($sql);
		$stmt->bind_param('i', $_GET['task_id']);

		$stmt->execute();

		header("location: index.php");
	}	
?>