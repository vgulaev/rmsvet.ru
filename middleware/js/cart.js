function al(){
	alert("Hello!!!");
}
cart = {
	deleterow : function ( di ) {
		var length = localStorage["cart.count"];
		if (length == undefined) length = 0;
		var i;
		for (i = di; i <= length - 2; i++) {
			localStorage["cart." + i + ".id"]		= localStorage["cart." + (i + 1) + ".id"];
			localStorage["cart." + i + ".count"]	= localStorage["cart." + (i + 1) + ".count"];
			localStorage["cart." + i + ".price"]	= localStorage["cart." + (i + 1) + ".price"];
			localStorage["cart." + i + ".caption"]	= localStorage["cart." + (i + 1) + ".caption"];
		};
		localStorage.removeItem("cart." + i + ".id");
		localStorage.removeItem("cart." + i + ".count");
		localStorage.removeItem("cart." + i + ".price");
		localStorage.removeItem("cart." + i + ".caption");
		localStorage["cart.count"] = length - 1;
		this.render();
	},
	getjson : function () {
		var sum = 0;
		var totalsum = 0;
		var length = localStorage["cart.count"];
		if (length == undefined) length = 0;
		var el = []; 
		for (var i = 0; i <= length - 1; i++) {
			var count = parseFloat(localStorage["cart." + i + ".count"]);
			var price = parseFloat(localStorage["cart." + i + ".price"]);
			sum = (count * price);
			totalsum = totalsum + sum;
			var newel = {"id" : localStorage["cart." + i + ".id"],
			"i"			: i,
			"caption"	: localStorage["cart." + i + ".caption"],
			"count"		: count,
			"price"		: price.toFixed(2),
			"sum"		: sum.toFixed(2)
			};
			el.push(newel);
		};
		return { "rows" : el, "totalsum" : totalsum, "length" : length};
	},
	render : function () {
		var rowhtml = "";
		var tbody = $("#goods");
		tbody.empty();
		var el = this.getjson();
		var template = $("#goods_tmpl").html();
  		Mustache.parse(template);
		var rendered = Mustache.render(template, {"el" : el["rows"], "totalsum" : el["totalsum"].toFixed(2), "length" : el["length"]});
		$("#goods").html(rendered);
	},
	create_order : function () {
        var el = this.getjson();
        $.ajax(
            {
                url: "/ws/write-order-to-srv",
                type: "POST",
                dataType: "json",
                data: {
                    "data" : JSON.stringify(el["rows"])
                },
                beforeSend: function () {
                }
            })
        .done(function ( data ) {
            if (data[ "r" ] === true ) {
                window.location.href = "/orders/" + data[ "id" ];
            }
            })
		//alert("Hey!!!");
        //window.location.href = "/"
	} 
};

$(function ()
{
	cart.render();
}
);


