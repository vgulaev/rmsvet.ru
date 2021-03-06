<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Корзина</title>
		<meta name="author" content="Valentin" />
		<script src="/libs/jquery/jquery-2.1.1.min.js"></script>
		<script src="/libs/mustache.js"></script>
		<script src="/js/common.js"></script>
		<script src="/js/query-obj.js"></script>
		<script src="/js/my.js"></script>
		<script src="/js/cart.js"></script>
		<script src="/js/fastsearch.js"></script>
		<link rel="stylesheet" type="text/css" href="css/main.css">
		<link rel="stylesheet" type="text/css" href="css/cart.css">
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
		<span class = "bt left20">
			<a id = "cart_label" href="/cart.html">
			<span>Товаров в корзине &nbsp;</span><span id = "cart_label_count"></span></a>
		</span>
		<span class = "bt left20"><a href="/contact.html">О нас</a></span>
		</span>
	</div>
	<div id = "output" class="main">
		<div class = "left100">
		<table class="cart_table mart10">
			<thead>
				<tr>
					<!--th>№</th-->
					<th>Товар</th>
					<th>Кол-во</th>
					<th>Цена</th>
					<th>Сумма</th>
				</tr>
			</thead>
			<script id="goods_tmpl" type="x-tmpl-mustache">
				{{#el}}
				<tr id = "{{ id }}">
					<td>
						<div class = "wp">
						<a href="/catalog/goods/{{ id }}">{{caption}}</a>
						</div>
						<div>
						<button onclick = "cart.deleterow({{ i }})">Удалить</button>
						</div>
					</td>
					<td class = "qty"><input class = "in_price" value = {{ count }} name = "{{ i }}" /></td>
					<td class = "num">{{ price }} </td>
					<td class = "num">{{ sum }} </td>
				</tr>
				{{/el}}
				<tr>
					<td colSpan = 3 class = "total">Всего ({{ length }} позиций)</td>
					<td class = "num">{{ totalsum }}</td>			
				</tr>
			</script>
			<tbody id = "goods">
			</tbody>
		</table>
		<div>
            <table class="cart_table">
                <tr>
                    <td>
            			<button onclick="cart.create_order()" >Купить</button>
	            		<!--button onclick = "">Выписать счет</button>
			            <button>Указать НДС</button-->
                    </td>
                    <td align="right">
                        <button onclick="cart.clear()" >Очистить корзину</button>
                    </td>
                </tr>
            </table>
		</div>

		<!--div>
			<span>Контрагент: </span><input id = "partner" class="partner" />
		</div>
		<div>
			<button onclick = "cart.write_to_srv()">Записать</button>
		</div-->
		</div>
	</div>
	</body>
</html>