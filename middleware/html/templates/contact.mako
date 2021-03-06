<%namespace name="globalv" file="global-vals.tmpl"/>
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
			<table>
				<tr>
					<td colspan="2"><span class="fn org">Логистрим ООО</span></td>
				</tr>
				<tr>
					<td>Директор:</td>
					<td>Гуляев Валентин Александрович</td>
				</tr>
				<tr>
					<td colspan="2">действует на основании устава</td>
				</tr>
				<tr>
					<td>ОГРН:</td>
					<td>1147232041296</td>
				</tr>
				<tr>
					<td>ИНН:</td>
					<td>7203318874</td>
				</tr>
				<tr>
					<td>КПП:</td>
					<td>720301001</td>
				</tr>
				<tr>
					<td colspan="2">Адрес местонахождения:</td>
				</tr>
				<tr>
					<td colspan="2">			
						<div class="adr">
						625048, Тюменская обл.,
						<span class="locality">г. Тюмень</span>,
						<span class="street-address">ул 50 лет Октября 8Б, <a href = "http://petrstol.ru/">ДД Петр Столыпин</a>, 1 этаж, территория EAZYSHOP</span>
						</div>
					</td>
				</tr>
				<tr>
					<td colspan="2">Юридический и Почтовый адрес:</td>
				</tr>
				<tr>
					<td colspan="2">
					625046, Тюменская обл., г Тюмень, ул. Широтная, д. 148, к. 3, кв. 205		
					</td>
				</tr>
				<tr>
					<td>Телефоны:</td>
					<td>
						<div>${globalv.attr.office_phone}</div>
						<div><span class="tel">+7-961-209-1778</span></div>
					</td>
				</tr>
				<tr>
					<td>E-mail:</td>
					<td><span class="email">vg@vgit.ru</span></td>
				</tr>
				<tr>
					<td colspan="2">
						<div>Мы работаем <span class="workhours">ежедневно с 9:00 до 18:00</span>
							<span class="url">
								<span class="value-title" title="http://ezsp.ru"> </span>
							</span>
						</div>
					</td>
				</tr>
			</table>
			<div>
				<a href="/cardrules.html">Правила оплаты картами Visa и Mastercard</a>
			</div>
			<div>
				<a href="/shipment.html">Правила доставки</a>
			</div>
			<div>
				<a href="/bible.html">Наши принципы</a>
			</div>
	</div>
	</body>
</html>