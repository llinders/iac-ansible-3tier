<!DOCTYPE html>
<html lang="en">
	<head>
		<!-- Bootstrap CSS -->
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1"/>

		<title>Simple todo app</title>
	</head>
	<body>
		<div class="col-md-3"></div>
		<div class="col-md-6 well">
			<h3 class="text-primary">PHP - Simple To Do List App</h3>
			<hr style="border-top:1px dotted #ccc;"/>
			<div class="col-md-2"></div>
			<div class="col-md-8">
				<center>
					<form method="POST" class="form-inline" action="add_query.php">
						<input type="text" class="form-control" name="task" required/>
						<button class="btn btn-primary form-control" name="add">Add Task</button>
					</form>
				</center>
			</div>
			<br /><br /><br />
			<?php 
			ini_set('display_errors', '1');
			ini_set('display_startup_errors', '1');
			error_reporting(E_ALL);
			echo 'test';
			?>
			<table class="table">
				<thead>
					<tr>
						<th>#</th>
						<th>Task</th>
						<th>Action</th>
					</tr>
				</thead>
				<tbody>
					<?php
						//$conn = pg_connect("host=192.168.1.54 port=5432 dbname=iac-db user=admin password=password") or die("Could not connect" . pg_last_error());
						//require 'conn.php';
						$conn = new mysqli('192.168.1.54', 'admin', 'admin-password', 'iac-db');
						var_dump($conn);
						$result = $conn->query("SELECT * FROM `Task` ORDER BY `id` ASC");
						$count = 1;
						if ($result->num_rows > 0) {
							while($row = $result->$fetch_assoc()){
					?>
					<tr>
						<td><?php echo $count++?></td>
						<td><?php echo $row?></td>
						<td><?php echo $row[0]?></td>
						<td><?php echo $row[1]?></td>
						<td><?php echo $row[2]?></td>
						<td colspan="2">
							<center>
								<a href="delete_query.php?task_id=<?php echo $row['id']?>" class="btn btn-danger"><span class="glyphicon glyphicon-remove"></span></a>
							</center>
						</td>
					</tr>
					<?php
							}
						} else {
							echo "0 results";
						}
					?>
				</tbody>
			</table>
		</div>
	</body>
</html>