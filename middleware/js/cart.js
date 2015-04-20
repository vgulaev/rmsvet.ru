function al(){
	alert("Hello!!!");
}
cart = {
	deleterow : function ( di, render) {
		if (render == null){
            render = true;
        }
        else{
            render = false;
        }
        var length = localStorage["cart.count"];
		if (length == undefined) length = 0;
		var i;
		for (i = di; i <= length - 2; i++) {
			localStorage["cart." + i + ".id"]		= localStorage["cart." + (i + 1) + ".id"];
			localStorage["cart." + i + ".count"]	= localStorage["cart." + (i + 1) + ".count"];
			localStorage["cart." + i + ".price"]	= localStorage["cart." + (i + 1) + ".price"];
			localStorage["cart." + i + ".caption"]	= localStorage["cart." + (i + 1) + ".caption"];
            localStorage["cart." + i + ".vat"]      = localStorage["cart." + (i + 1) + ".vat"];
		};
		localStorage.removeItem("cart." + i + ".id");
		localStorage.removeItem("cart." + i + ".count");
		localStorage.removeItem("cart." + i + ".price");
		localStorage.removeItem("cart." + i + ".caption");
        localStorage.removeItem("cart." + i + ".vat");
		if (localStorage["cart.count"] > 0){
            localStorage["cart.count"] = length - 1;
        }
        else{
            localStorage["cart.count"] = 0;
        }
        if (render){
        this.render();
        }
	},
    clear : function(){
        for (var i = localStorage["cart.count"]; i>=0; i--){
            cart.deleterow(i, false);
        localStorage["cart.count"] = 0;
        this.render()
        }
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
			"sum"		: sum.toFixed(2),
            "vat"       : localStorage["cart." + i + ".vat"]
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
		$( "#goods" ).html( rendered );
        $( ".in_price" ).on( "input", function () {
            if (this.value > 0) {
                localStorage["cart." + this.name + ".count"] = this.value;
                cart.render();
                var SearchInput = $( "input[name='" + this.name + "']" );
                var strLength= SearchInput.val().length * 2;
                SearchInput.focus();
                SearchInput[0].setSelectionRange(strLength, strLength);
            }
        });
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
	} 
};

$(function ()
{
	cart.render();
}
);