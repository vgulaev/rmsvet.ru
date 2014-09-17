function fint_view() {
    var e = $("#core");
    var toppx = Math.round($(window).height() - $("#SearchStr").height())/2;
    var left = Math.round(($(window).width() - 520)/2);
    e.css({position: "absolute",left: left + "px", top: toppx + "px"})
};

$( window ).resize( function () {
    if ($("#SearchStr").val() == "")
        fint_view();
});

$( function () {
    $("#SearchStr").on("input", function () {
            my();
            if ($("#SearchStr").val() == "") {
                fint_view();
                $("#secondline").hide();
                $("#output").hide();
                //$("#core").css({position: "inherit"});
            }
            else {
                $("#core").css({position: "inherit"});
                $("#secondline").show();
                $("#output").show();
            };
            //$("#output").html( $("#SearchStr").val() );
        })
    class_cart_label.create();
    fint_view();
    $("#SearchStr").focus();
    var qs = getParameterByName("q");
    if (qs != "") {
        $("#SearchStr").val(qs);
        $("#core").css({position: "inherit"});
        $("#secondline").show();
        $("#output").show();
        my();
    };
}
);