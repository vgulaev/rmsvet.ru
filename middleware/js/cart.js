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
	render : function () {
		var length = localStorage["cart.count"];
		var rowhtml = "";
		var tbody = $("#goods");
		var sum = 0;
		var totalsum = 0;
		tbody.empty();
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
		var template = $("#goods_tmpl").html();
  		Mustache.parse(template);
		var rendered = Mustache.render(template, {"el" : el, "totalsum" : totalsum.toFixed(2), "length" : length});
		$("#goods").html(rendered);
	}
};

$(function ()
{
	cart.render();
}
);


