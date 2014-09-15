class_cart_label = {
    create: function () {
        this.html_element = $("#cart_label")[0];
        this.cart_label_count = $(this.html_element).find("#cart_label_count");
        this.count = localStorage["cart.count"]
        if (this.count == undefined) {
            this.count = 0;
        };
        this.cart_label_count.html(this.count);
    },
    add_item : function ( id ) {
        var clc = $(this).find("#cart_label_count");
        localStorage["cart." + this.count + ".id"] = id;
        localStorage["cart." + this.count + ".count"] = 1;
        localStorage["cart." + this.count + ".caption"] = $("#caption").html();
        localStorage["cart." + this.count + ".price"] = $("#price").html();
        this.count++;
        localStorage["cart.count"] = this.count;
        this.cart_label_count.html(this.count);
    }
}

function add_to_cart( id ) {
    class_cart_label.add_item( id );
}
function currency_sym( cur ) {
    if (cur == "USD"){
        res = "$"
    }
    else {
        res = "₽"
    }
    return res;
}

function make_element_for_main_page( obj ) {
    var rowhtml = [
    "<div class = \"left100 width430 mart10\">",
    "<a href=\"/" + obj.fantastic_url + "/goods\">",
        "<div>",
            //"<span id = \"caption\">" + obj.caption.substring(0, 20) + "</span><span>" + obj.caption.substring(20) + "</span>",
            "<span id = \"caption\">" + obj.caption + "</span>",
        "</div>",
        "<div>",
            "<span>" + currency_sym(obj.currency) + " &nbsp;</span><span id = \"price\">" + obj.price + "</span>", 
        "</div>",
        "</a>",
    "</div>",
    ].join('\n');  
    "<p><span id = \"caption\">" + obj.caption.substring(0, 20) + "</span><span id =- \"price\">" + obj.price + "</span></p>"
    //return "<p>" + obj.caption.substring(0, 20) + "</p>";
    return rowhtml;
}
function my() {
    //alert("Hello!!!");
    $.ajax(
        {
            url: "/ws/autocomplate",
            type: "POST",
            dataType: "json",
            data: {
                "table": "goods",
                "filter" : $("#SearchStr").val()
            }
        })
    .done(function ( data ) {
        $("#output").empty();
        for (var e in data.goods) {
            var el = make_element_for_main_page( data.goods[e] );
            $("#output").append(el);
        }
        //alert("Done");
    })
    .success(
        )
    .always( function () {
        //alert("!!!");
    }
        );
};

function makeid()
{
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < 5; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}

function test_500ajax() {
    for (var i = 0; i < 2000; i++) {
        $("#SearchStr").val(makeid());
        my();
    };
}