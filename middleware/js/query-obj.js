var _templ = {
    main                    : "",
    result_list             : "",
    filter_main             : "",
    filter_list             : "",
    filter_type_and_values  : ""
};

function load_templs() {
    $.get('/query-obj/main.html', function ( template ) {
        _templ.main = template;
    });

    $.get('/query-obj/result-list.html', function ( template ) {
        _templ.result_list = template;
    });

    $.get('/query-obj/filter-main.html', function ( template ) {
        _templ.filter_main = template;
    });

    $.get('/query-obj/filter-list.html', function ( template ) {
        _templ.filter_list = template;
    });

    $.get('/query-obj/filter-type-and-values.html', function ( template ) {
        _templ.filter_type_and_values = template;
    });
}

load_templs();

var ezsp_query_com = {
    server : {
        //query string
        q : "",
        //uses filters
        uf: [],
        //orders
        o : []
    },
    client : {
        //filters
        f : [],
        //result
        r : []
    },
};

/*function hz( things ) {
    alert( things );
    return false;
}*/

var filters_manager = {
    query_to_server : function () {
        ezsp_query_com.r = [];
        ezsp_query_com.f = [];
        $.ajax(
            {
                url: "/ws/ezsp-query-filters-value",
                type: "POST",
                dataType: "json",
                data: {
                    "ezsp-query" : JSON.stringify(ezsp_query.query)
                },
                beforeSend: function () {
                }
            })
        .done(function ( data ) {
            alert("Yes");
            })
        .always(function () {
        });
    },
    addfilter : function ( index ) {
        $( "#filter_name" ).val( ezsp_query.ans.f.items[index].name );
        ezsp_query.query.f.push(ezsp_query.ans.f.items[index]);
        filters_manager.query_to_server();
        return false;
    },
    filter_list : function ( things ) {
        var res;
        var sub = $( "#filter_name" ).val();
        if (sub === "") {
            res = things;
        }
        else {
            res = [];
            for (var i = 0; i < things.length; i++) {
                if (things[i].name.toLowerCase().indexOf(sub) != -1) { 
                    res.push(things[i]);
                }
            }
        }
        return res;
    },
    render_list : function () {
        var rendered = Mustache.render(_templ.filter_list, {"items": filters_manager.filter_list(ezsp_query.ans.f.items)});
        $( "#filter-list" ).html( rendered );
    },
    init : function () {
        //var rendered = Mustache.render(_templ.filter_main, {"items": ezsp_query_com.f.items});
        $( "#result-list" ).html(_templ.filter_main);
        $( "#filter_name" ).on( "input", function () {
                filters_manager.render_list();
            });
        filters_manager.render_list();
    }
};

function rand_id() {
    return Math.floor( Math.random() * 10000 );
}

function link_input_prices_range( ) {
    $( "#price_from" ).on( "input", function () {
        ezsp_query.query.p.price_from = $( "#price_from" ).val();
        ezsp_query.query_to_server();
    } );
    $( "#price_to" ).on( "input", function () {
        ezsp_query.query.p.price_to = $( "#price_to" ).val();
        ezsp_query.query_to_server();
    } );
    $( "#supplier" ).on( "input", function () {
        ezsp_query.query.p.supplier = $( "#supplier" ).val();
        ezsp_query.query_to_server();
    } );
    $( "#order_asc" ).change( function () {
        if ( this.checked ) {
            $( "#order_desc" ).prop( "checked", false )
            ezsp_query.query.p.order_price = "asc";
            ezsp_query.query_to_server();
        }
        //ezsp_query.query.p.supplier = $( "#supplier" ).val();
        //
    } );
    $( "#order_desc" ).change( function () {
        if ( this.checked ) {
            $( "#order_asc" ).prop( "checked", false )
            ezsp_query.query.p.order_price = "desc";
            ezsp_query.query_to_server();
        }
        //ezsp_query.query.p.supplier = $( "#supplier" ).val();
        //ezsp_query.query_to_server();
    } );
}

var ezsp_query = {
    na : 0,
    np : 0,
    query : {
        id : 0,
        q : "",
        f : [],
        p : {}
    },
    ans : {
        r : [],
        f : {
        items : []
    }
    }, 
    ajaxing : false,
    render_init : function () {
        $( "#output" ).html( _templ.main );
        link_input_prices_range();
    },
    addfilter : function () {
        filters_manager.init();
    },
    update_add_filter_button: function () {
        $( "#add_filter_button" ).html("Добавить один из " + ezsp_query.ans.f.items.length + " фильтров");
    },
    render : function ( data ) {
        ezsp_query.ans = data;
        var cont = $( "#result-list" );
        if (cont.length === 0) {
            ezsp_query.render_init();
            cont = $( "#result-list" );
        }
        var rendered = Mustache.render(_templ.result_list, {"items": ezsp_query.ans.r.goods});
        ezsp_query.update_add_filter_button();
        cont.html(rendered);
    },
    query_to_server : function () {
        if ( ezsp_query.ajaxing === false ) {
            $.ajax(
                {
                    url: "/ws/ezsp-query",
                    type: "POST",
                    dataType: "json",
                    data: {
                        "ezsp-query" : JSON.stringify( ezsp_query.query )
                    },
                    beforeSend: function () {
                        ezsp_query.ajaxing = true;
                        return true;
                    }
                })
            .done(function ( data ) {
                if ( data.q_id != ezsp_query.query.id ) {
                    ezsp_query.ajaxing = false;
                    ezsp_query.query_to_server( );
                }
                else {
                    ezsp_query.render(data);
                }
            })
            .always(function () {
                ezsp_query.ajaxing = false;
            });
        }
        else {
            ezsp_query.query.id = rand_id();
        }
        //alert($(ezsp_query.input_id).val());
    },
    link_input : function ( id ) {
        ezsp_query.input_id = id;
        $( id ).on( "input", function () {
                var qs = $( ezsp_query.input_id ).val();
                location.hash = "q=" + qs;
                ezsp_query.query.q = qs;
                ezsp_query.query_to_server();
                //console.log( ezsp_query.np++ );
            });
    },
    output_id : "",
    input_id : ""
};