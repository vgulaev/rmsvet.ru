function rotatelogo_Z ( ) {
    var rd = 1;
    var intervalID = window.setInterval( function () {
        rd = ( rd + 1 ) % 360;
        console.log( rd );
        $( "#logo_Z" ).css( "-webkit-transform", "rotate(" + rd + "deg)" );
    }, 50);

    //alert( "G" );
}

function create_input_search( ) {
    
}

$( function ( ) {
    $( "#main_magnifier ").hover( function () {
        create_input_search( );
    } );
});