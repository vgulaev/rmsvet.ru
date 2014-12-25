<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Контакты</title>
		<meta name="author" content="Valentin" />
		<script src="/libs/jquery/jquery-2.1.1.min.js"></script>
		<script src="/libs/mustache.js"></script>
		<script src="/js/common.js"></script>
		<script src="/js/query-obj.js"></script>
		<script src="/js/my.js"></script>
		<!--script src="/js/cart.js"></script-->
		<script src="/js/fastsearch.js"></script>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<!--link rel="stylesheet" type="text/css" href="/css/cart.css"-->
	</head>
	<body>
	<%include file="yandex-metrika.tmpl"/>
	<div id = "core">
		<span class = "fc">Ваш запрос:</span><input id = "SearchStr">
	</div>
	<div id = "secondline">
		<span>
		<span class = "bt left100 right20">Информация о товаре</span>
		<span class = "bt left20">Действия на сайте</span>
		<span class = "bt left20"><a id = "cart_label" href="/cart.html"><span>Товаров в корзине &nbsp;</span><span id = "cart_label_count"></span></a></span>
		<span class = "bt left20"><a href="/contact.html">О нас</a></span>
		</span>
	</div>
	<div id = "output" class="main">
		<div class="vcard left100">
		<%include file="ezsp_for_everybody/content.tmpl"/>
		</div>
	</div>
	</body>
</html>