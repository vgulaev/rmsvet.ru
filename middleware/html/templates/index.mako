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
	</head>
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
		<!--a href="" class = "vs-mc-a" onclick="javascript:window.open('/html/vbvhelp.html','Chargeback','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width=450,height=400');">
		<img class = "img-vs-mc" src="/gif/mcvs/visa_logo.gif">
		<img class = "img-vs-mc" src="/gif/mcvs/visa_verified.gif">
		</a>
		<a href="" class = "vs-mc-a" onclick="javascript:window.open('http://www.mastercardbusiness.com/mcbiz/index.jsp?template=/orphans&content=securecodepopup','Chargeback','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width=550,height=380')">
		<img class = "img-vs-mc" src="/gif/mcvs/mc_logo.gif">
		<img class = "img-vs-mc" src="/gif/mcvs/mc_securecode.gif">
		</a-->
	</div>
	</body>
</html>

