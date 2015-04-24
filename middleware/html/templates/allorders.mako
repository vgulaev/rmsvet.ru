<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Список заказов</title>
	</head>
	<body>
	<table border="2">
	<tr>
        <th>ID</th>
        <th>Number</th>
        <th>Date</th>
        <th>Organization</th>
        <th>Partner</th>
    </tr>
	{{#allorders}}
		<tr align="center">
            <td>{{id}}</td>
            <td>{{number}}</td>
            <td>{{date}}</td>
            <td>{{organization}}</td>
            <td>{{partner}}</td>
        </tr>
	{{/allorders}}
	</table>
	</body>
</html>
