function fint_view() {
    var e = $("#core");
    var toppx = Math.round($(window).height() - $("#SearchStr").height())/2;
    var left = Math.round(($(window).width() - 520)/2);
    e.css({position: "absolute",left: left + "px", top: toppx + "px"})
};

function work_state() {
    $("#core").css({position: "inherit"});
    $("#secondline").show();
    $("#output").show();
}

$( window ).resize( function () {
    if ($("#SearchStr").val() == "")
        fint_view();
});

$( function () {
    $("#SearchStr").on("input", function () {
            //my();
            work_state();
        })
    class_cart_label.create();
    fint_view();
    $("#SearchStr").focus();
    var qs = getParameterByName("q");
    if (qs != "") {
        $("#SearchStr").val(qs);
        work_state();
        ezsp_query_com.q = qs;
        ezsp_query.query_to_server();
        //my();
    };
    ezsp_query.link_input("#SearchStr");
    ezsp_query.link_output = "#output";
});