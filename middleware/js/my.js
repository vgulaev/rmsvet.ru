function my() {
    //alert("Hello!!!");
    $.ajax(
        {
            url: "ws/autocomplate",
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
            var el = "<p>" + data.goods[e].caption + "</p>";
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