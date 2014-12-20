function onvoice(argument) {
    var recognition = new webkitSpeechRecognition();
    recognition.lang = "ru";
    recognition.onresult = function( speechData ) { 
      if (speechData.results.length > 0) {
        var sra = speechData.results[0];
        if (sra.length > 0) {
            var mytext = sra[0].transcript;
            //console.log( mytext )
            $( "#SearchStr" ).val( mytext );
            $( "#SearchStr" ).trigger( "input" ); 
        }
      }
      //console.log(event) 
    }
    recognition.start();
    //alert("try");
}

function fint_view() {
    var e = $("#core");
    var toppx = Math.round($(window).height() - $("#SearchStr").height())/2;
    var left = Math.round(($(window).width() - 520)/2);
    e.css({position: "absolute",left: left + "px", top: toppx + "px"});
}

function work_state() {
    $("#core").css({position: "inherit"});
    $("#secondline").show();
    $("#output").show();
    $("#cardinfo").hide();    
}

$( window ).resize( function () {
    if ($("#SearchStr").val() === "")
        fint_view();
});

$( function () {
    $("#SearchStr").on("input", function () {
            //my();
            work_state();
        });
    class_cart_label.create();
    fint_view();
    $("#SearchStr").focus();
    var qs = getParameterByName("q");
    if (qs !== "") {
        $("#SearchStr").val(qs);
        work_state();
        ezsp_query.query.q = qs;
        ezsp_query.query_to_server();
        //my();
    }
    ezsp_query.link_input("#SearchStr");
    ezsp_query.link_output = "#output";
});