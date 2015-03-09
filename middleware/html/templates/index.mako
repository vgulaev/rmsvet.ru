<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Торгуй легко</title>
		<meta name="author" content="Valentin" />
		<meta name="page" content="index" />
		<script src="/libs/jquery/jquery-2.1.1.min.js"></script>
		<script src="/libs/mustache.js"></script>
		<script src="/js/common.js"></script>
		<script src="/js/query-obj.js"></script>
		<script src="/js/my.js"></script>
		<script src="/js/index.js"></script>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="search" href="/opensearch.xml" title="ezsp" type="application/opensearchdescription+xml">	</head>
	<body>
	<%include file="yandex-metrika.tmpl"/>
	<div id = "core">
		<span class = "fc">Ваш запрос:</span><input id = "SearchStr">
		<button id = "speechButton" onclick = "onvoice()">Голос</button>
	</div>
	<div id = "secondline" style="display: none;">
		<span>
		<span class = "bt left100 right20">Поиск товаров</span>
		<span class = "bt left20">Действия на сайте</span>
		<span class = "bt left20">
			<a id = "cart_label" href="/cart.html"><span>Товаров в корзине &nbsp;</span><span id = "cart_label_count"></span></a>
		</span>
		<span class = "bt left20"><a href="/contact.html">О нас</a></span>
		</span>
	</div>
	<div id = "output" class="main" style="display: none;">
	</div>
	<div id = "cardinfo">
		<a href="/site-map/">Карта сайта</a>
		<a href="/contact.html">О нас</a>
		<!-- a href="/ezsp_for_everybody.html">EZSP каждому</a -->
	</div>
	</body>
</html>

