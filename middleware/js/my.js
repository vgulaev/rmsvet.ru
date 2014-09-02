function make_element_for_main_page( obj ) {
    var rowhtml = [
    "<div>",
    "<a href=\"/catalog/goods/" + obj.id + "\">",
        "<div>",
            "<span id = \"caption\">" + obj.caption.substring(0, 20) + "</span>",
        "</div>",
        "<div>",
            "<span>₽ </span><span id = \"price\">" + obj.price + "</span>", 
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

$( function () {
    $("#SearchStr").on("input", function () {
            my();
            $("#output").html( $("#SearchStr").val() );
        })
}
);