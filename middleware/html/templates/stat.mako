<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Project statistic</title>
	</head>
	<body>
	<table border="2" bgcolor="559922">
	<tr  align="center" bgcolor="AAAAFF"><td bgcolor="FFFF00">формат</td><td>файлы</td><td>строки</td><td>$</td><td>автор</td><td>строки</td><td>$</td></tr>
	{{#stats1}}
		<tr align="center" bgcolor="AAFFAA"><td rowspan="4">{{ext}}</td><td rowspan="4">{{items}}</td><td rowspan="4">{{lines1}}</td><td rowspan="4">{{dol1}}</td></tr>
		{{#avtor}}
			<tr bgcolor="00AA00"><td>{{name}}</td><td>{{lines2}}</td><td>{{dol2}}</td></tr>
		{{/avtor}}
	{{/stats1}}
	<tr align="center"  bgcolor="FF0000"><td rowspan="4">Всего</td><td rowspan="4">{{allitems}}</td><td rowspan="4">{{total}}</td><td rowspan="4">{{dol}}</td></tr>
	{{#all}}
		<tr bgcolor="FF0000"><td>{{name3}}</td><td>{{lines3}}</td><td>{{dol3}}</td></tr>
	{{/all}}
	</table>
	</body>
</html>
