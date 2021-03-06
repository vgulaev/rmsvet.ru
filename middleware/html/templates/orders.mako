<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Заказ</title>
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
    <%include file="core.tmpl"/>
    <%include file="secondline.tmpl"/>
    <div id = "output" class="main">
        <div class = "left100">
        <div>Номер заказа: <span><b>{{order.number}}</b></span> от <span><b>{{order.date}}</b></span></div>
        <div class="wp cart_table">Поставщик: <b>ООО "Логистрим", ИНН 7203318874, КПП 720301001, 625046, Тюменская обл, Тюмень г, Широтная ул, дом № 148, корпус 3, квартира 205, тел.: +7-961-209-1778</b></div>
        <div class="wp cart_table">Покупатель: <b>{{partner.caption}}</b></div>
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
                        {{good}}
                        </div>
                    </td>
                    <td class = "qty">{{ quantity }}</td>
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
            <!-- Значения всех полей условны и приведены исключительно для примера --> 
            <form action="https://money.yandex.ru/eshop.xml" method="post"> 
              
            <!-- Обязательные поля --> 
            <input name="shopId" value="20820" type="hidden"/> 
            <input name="scid" value="11033" type="hidden"/> 
            <input name="sum" value="{{ totalsum }}" type="hidden"> 
            <input name="customerNumber" value="{{partner.caption}}" type="hidden"/>
            
            <!-- Необязательные поля --> 
            <input name="orderNumber" value="{{order.number}}" type="hidden"/>
            <input name="paymentType" value="AC" type="hidden"/>
              
            <!--input name="shopArticleId" value="567890" type="hidden"/> 
            <input name="paymentType" value="AC" type="hidden"/> 
            <input name="orderNumber" value="abc1111111" type="hidden"/> 
            <input name="cps_phone" value="79110000000" type="hidden"/> 
            <input name="cps_email" value="user@domain.com" type="hidden"/--> 
              
            <input type="submit" value="Оплать Visa/MasterCard"/> 
            </form>
            <form action="https://money.yandex.ru/eshop.xml" method="post"> 
              
            <!-- Обязательные поля --> 
            <input name="shopId" value="20820" type="hidden"/> 
            <input name="scid" value="11033" type="hidden"/> 
            <input name="sum" value="{{ totalsum }}" type="hidden"> 
            <input name="customerNumber" value="{{partner.caption}}" type="hidden"/>
            
            <!-- Необязательные поля --> 
            <input name="orderNumber" value="{{order.number}}" type="hidden"/>
            <input name="paymentType" value="PC" type="hidden"/>
              
            <!--input name="shopArticleId" value="567890" type="hidden"/> 
            <input name="paymentType" value="AC" type="hidden"/> 
            <input name="orderNumber" value="abc1111111" type="hidden"/> 
            <input name="cps_phone" value="79110000000" type="hidden"/> 
            <input name="cps_email" value="user@domain.com" type="hidden"/--> 
              
            <input type="submit" value="Оплать Яндекс.Деньги"/> 
            </form>
            <a href = "/getorderspdf/{{order.id}}">Скачать счет в pdf</a>
        </div>
        </div>
    </div>
    </body>
</html>