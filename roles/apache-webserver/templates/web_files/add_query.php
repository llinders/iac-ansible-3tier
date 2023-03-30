<?php
	require_once 'conn.php';
	if(ISSET($_POST['add'])){
		if($_POST['task'] != ""){
			
			$sql = 'INSERT INTO Task (task) VALUES (?)';
			$stmt = $conn->prepare($sql);
			$stmt->bind_param('s', trim($_POST['task']));

			$stmt->execute();
			
			header('Location: index.php');
		}
	}
?>