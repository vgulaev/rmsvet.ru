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
	make_td_for_caption : function ( i ) {
		var res = ["<div>",
		"<a href=\"/catalog/goods/" + localStorage["cart." + i + ".id"] + "\">" + localStorage["cart." + i + ".caption"] + "</a>",
		"</div>",
		"<div>",
		"<button onclick = \"cart.deleterow(" + i + ")\">Удалить</button>",
		"</div>"
		].join('\n');
		return 	res;
	},
	render : function () {
		var length = localStorage["cart.count"];
		var rowhtml = "";
		var tbody = $("#goods");
		var sum = 0;
		var totalsum = 0;
		tbody.empty();
		if (length == undefined) length = 0; 
		for (var i = 0; i <= length - 1; i++) {
			var count = parseFloat(localStorage["cart." + i + ".count"]);
			var price = parseFloat(localStorage["cart." + i + ".price"]);
			sum = (count * price);
			totalsum = totalsum + sum;
			rowhtml = ["<tr id = " + localStorage["cart." + i + ".id"] + ">",
					"<td>" + (i + 1) + "</td>",
					"<td>" + this.make_td_for_caption(i) + "</td>",
					"<td>" + count + "</td>",
					"<td class = \"num\">" + price.toFixed(2) + "</td>",
					"<td id = \"sum\" class = \"num\">" + sum.toFixed(2) + "</td>",
				"</tr>"].join('\n');
			tbody.append(rowhtml);
		};
		rowhtml = ["<tr>",
		"<td colSpan = 4>Всего</td>",
		"<td class = \"num\">" + totalsum.toFixed(2) + "</td>",
		"</tr>"
		].join('\n');
		tbody.append(rowhtml); 
	}
};

$(function ()
{
	cart.render();
}
);


