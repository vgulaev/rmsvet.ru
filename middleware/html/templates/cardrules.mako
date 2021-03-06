<%namespace name="globalv" file="global-vals.tmpl"/>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Пластиковые карты</title>
		<meta name="author" content="Valentin" />
		<script src="/libs/jquery/jquery-2.1.1.min.js"></script>
		<script src="/libs/mustache.js"></script>
		<script src="/js/common.js"></script>
		<script src="/js/query-obj.js"></script>
		<script src="/js/my.js"></script>
		<script src="/js/cart.js"></script>
		<script src="/js/fastsearch.js"></script>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/cart.css">
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
		<div class="left100" style="width: 40%; text-align: justify;">
		Правила оплаты
		<ol>
			<li><span>Описание процесса платежа</span>
			<div>
			Оплата происходит через авторизационный сервер Процессингового центра Банка с использованием Банковских кредитных карт следующих платежных систем:
			<ul>
				<li>VISA International</li>
				<li>MasterCard Worldwide</li>
			</ul>
			</div>
			</li>
			<li>Описания процесса передачи данных
			<div>
			Для осуществления платежа Вам потребуется сообщить данные Вашей пластиковой карты. Передача этих сведений производится с соблюдением всех необходимых мер безопасности. Данные будут сообщены только на авторизационный сервер Банка по защищенному каналу (протокол SSL 3.0). Информация передается в зашифрованном виде и сохраняется только на специализированном сервере платежной системы. Сайты и магазины не знают и не хранят данные по Вашей пластиковой карте.	
			</div>
			</li>
			<li>Возврат оплаты в случае отказа клиентом от товара/услуги
			<div>
			Необходимо оформить заявку на возврат по номеру телефона ${globalv.attr.office_phone}. Сообщить:
			<ul>
				<li>Номер заказа</li>
				<li>Дата заказа</li>
				<li>ФИО или ИНН организации</li>
				<li>Причина возврата</li>
			</ul>
			Возврат денежных средств производится на ту карту, с корой ранее произвели оплату.
			</div>
			</li>
		</ol>
		</div>
	</div>
	</body>
</html>