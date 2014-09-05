cart = {
	make_td_for_caption : function ( i ) {
		/*<div></div>
		<div>
		<a>О товаре</a>
		<a>О товаре</a>
		</div>*/
		return 	localStorage["cart." + i + ".caption"];
	},
	render : function () {
		var length = localStorage["cart.count"]
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
					"<td>" + price + "</td>",
					'<td id = "sum">' + sum.toFixed(2) + "</td>",
				"</tr>"].join('\n');
			tbody.append(rowhtml);
		};
		rowhtml = ["<tr>",
		"<td colSpan = 4>Всего</td>",
		"<td>" + totalsum + "</td>",
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


