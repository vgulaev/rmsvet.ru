def index():
	res = """<!DOCTYPE html>
	<html lang="ru">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
			<title>ТюменьАгромаш</title>
			<meta name="author" content="Valentin" />
			<meta name="page" content="index" />
			<meta name="viewport" content="width=device-width, initial-scale=1">
			</head>
		<body>"""
	f = open( "tam/report.req", "r", encoding = "utf-8" )
	res += f.read()
	res += "</body></html>"
	return res

def test():
	return "Hello"