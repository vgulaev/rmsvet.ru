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
        if (localStorage["cart.count"] == null){
            localStorage["cart.count"] = 0;}
        if (isNaN(localStorage["cart.count"])){
            localStorage["cart.count"] = 0;}
        this.count = localStorage["cart.count"];
        var flag = true;
        for ( var i = 0; i < this.count; i++ ){
            if (localStorage["cart." + i + ".id"] == id){
                flag = false;
                localStorage["cart." + i + ".count"]++;
                break;
            }
        }
        if ( flag ){
            localStorage["cart." + this.count + ".id"] = id;
            localStorage["cart." + this.count + ".count"] = 1;
            localStorage["cart." + this.count + ".caption"] = $("#caption").html();
            localStorage["cart." + this.count + ".price"] = $("#price").html();
            localStorage["cart." + this.count + ".vat"] = $("#vat").html();
            this.count++;
            localStorage["cart.count"] = this.count;
            this.cart_label_count.html(this.count);
        }
    },
    add_item_from_list : function ( id, caption, price, vat ) {
        if (localStorage["cart.count"] == null){
            localStorage["cart.count"] = 0;}
        if (isNaN(localStorage["cart.count"])){
            localStorage["cart.count"] = 0;}
        this.count = localStorage["cart.count"];
        var flag = true;
        for ( var i = 0; i < this.count; i++ ){
            if (localStorage["cart." + i + ".id"] == id){
                flag = false;
                localStorage["cart." + i + ".count"]++;
                break;
            }
        };
        if ( flag ){
            localStorage["cart." + this.count + ".id"] = id;
            localStorage["cart." + this.count + ".count"] = 1;
            localStorage["cart." + this.count + ".caption"] = caption;
            localStorage["cart." + this.count + ".price"] = price;
            localStorage["cart." + this.count + ".vat"] = vat;
            this.count++;
            localStorage["cart.count"] = this.count;
            this.cart_label_count.html(this.count);
        };
    }
}

function add_item_from_list( id, caption, price, vat ) {
    class_cart_label.add_item_from_list( id, caption, price, vat );
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

function getfilters() {
    $.ajax(
        {
            url: "/ws/getfilters",
            type: "POST",
            dataType: "json",
            data: {
                "filter" : $("#SearchStr").val()
            }
        })
    .done(function ( data ) {
        $("#filters").empty();
        $.get('/html/filter.html', function(template) {
            var rendered = Mustache.render(template, {"items": data.items});
            $("#filters").html(rendered);
            //getfilters();
          });
        });
}

filters = {
    items : []
}

function my() {
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
        $.get('/html/search_goods.html', function(template) {
            var rendered = Mustache.render(template, {"items": data.goods});
            $("#output").html(rendered);
            getfilters();
          });
        })
    .success()
    .always();
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
        //my();
        ezsp_query.query_to_server();
    };
}