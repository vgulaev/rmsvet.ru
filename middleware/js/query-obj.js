_templ = {
    main                    : "",
    result_list             : "",
    filter_main             : "",
    filter_list             : "",
    filter_type_and_values  : ""
};

function load_templs() {
    $.get('/html/query-obj/main.html', function ( template ) {
        _templ.main = template;
    });

    $.get('/html/query-obj/result-list.html', function ( template ) {
        _templ.result_list = template;
    });

    $.get('/html/query-obj/filter-main.html', function ( template ) {
        _templ.filter_main = template;
    });

    $.get('/html/query-obj/filter-list.html', function ( template ) {
        _templ.filter_list = template;
    });

    $.get('/html/query-obj/filter-type-and-values.html', function ( template ) {
        _templ.filter_type_and_values = template;
    });
};

load_templs();

ezsp_query_com = {
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

function hz( things ) {
    alert( things );
    return false;
}

filters_manager = {
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
        var sub = $( "#filter_name" ).val();
        if (sub == "") {
            res = things;
        }
        else {
            res = [];
            for (var i = 0; i < things.length; i++) {
                if (things[i].name.toLowerCase().indexOf(sub) != -1) { 
                    res.push(things[i]);
                };
            };
        };
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
}

ezsp_query = {
    na : 0,
    np : 0,
    query : {
        q : "",
        f : []
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
        if (cont.length == 0) {
            ezsp_query.render_init();
            cont = $( "#result-list" );
        }
        var rendered = Mustache.render(_templ.result_list, {"items": ezsp_query.ans.r.goods});
        ezsp_query.update_add_filter_button();
        cont.html(rendered);
    },
    query_to_server : function () {
        $.ajax(
            {
                url: "/ws/ezsp-query",
                type: "POST",
                dataType: "json",
                data: {
                    "ezsp-query" : JSON.stringify(ezsp_query.query)
                },
                beforeSend: function () {
                    res = false;
                    if (ezsp_query.ajaxing == false) {
                        ezsp_query.ajaxing = true;
                        res = true;
                    }
                    return res;
                }
            })
        .done(function ( data ) {
            if ( data.q != ezsp_query.query.q ) {
                ezsp_query.query_to_server();
            }
            else {
                ezsp_query.render(data);
            }
            //console.log( ezsp_query.na++ );
            })
        .always(function () {
            ezsp_query.ajaxing = false;
            //alert( "always" );
        });
        //alert($(ezsp_query.input_id).val());
    },
    link_input : function ( id ) {
        ezsp_query.input_id = id;
        $( id ).on( "input", function () {
                ezsp_query.query.q = $( ezsp_query.input_id ).val();
                ezsp_query.query_to_server();
                //console.log( ezsp_query.np++ );
            })
    },
    output_id : "",
    input_id : ""
};