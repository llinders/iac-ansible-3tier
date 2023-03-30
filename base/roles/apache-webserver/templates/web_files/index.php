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
			<h3 class="text-primary">Todo list</h3>
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
						require 'conn.php';
						$result = $conn->query("SELECT * FROM `Task` ORDER BY `id` ASC");
						$count = 1;
						if ($result->num_rows > 0) {
							while($row = $result->fetch_assoc()){
					?>
					<tr>
						<td><?php echo $count++?></td>
						<td><?php echo $row["task"]?></td>
						<td>
							<a href="delete_query.php?task_id=<?php echo $row['id']?>" class="btn btn-danger">
								<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
									<path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
									<path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
								</svg>
								Delete
							</a>
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