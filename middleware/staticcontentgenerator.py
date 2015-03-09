# -*- coding: utf-8 -*-
import common as cm
import pystache
import statistics
import urllib
import dbclasses.dbobj
import dbclasses.dbworker

def _h(s):
    return str(s).replace("<", "").replace(">", "")

def html_view_for_addfld( id ):
    sql = "select * from properties where priceref = %(id)s"
    db = dbclasses.dbworker.getcon()
    cursor = db.cursor()
    cursor.execute( sql, { "id" : id } )
    row = cursor.fetchone()
    res = []
    while (row is not None):
        if not (row[1][0 : 2] == "__"):
            el = {"name" : row[2], "value" : row[3]}
            res += [el]
        row = cursor.fetchone()
    cursor.close()
    #el = {"name" : "organization", "value" : cm.env["organization"]}
    #res += [el]
    return res

def  goods_main_view(url, url_type = None):
    _templ_res = cm.read_file_to_str("html/goods_main_view.html")
    obj = dbclasses.dbobj.objects[ "prices" ]()
    img = dbclasses.dbobj.objects[ "images" ]()
    id = url[-36:] 
    res = False
    if (url_type == "id"):
        res = obj.find( id = id )
    else:
        u = url[ 1:-6]
        res = obj.find( fantastic_url = u )
    #res = _templ_res.format(gd = obj, addfld = html_view_for_addfld(id))
    img_url = "/png/nophoto.png"
    if img.find( priceref = obj.id ):
        img_url = img.url.val
    #html_view_for_addfld( obj.id )
    if res == True:
        res = pystache.render(_templ_res, {"gd" :  obj.__dict__ , "addfld" : html_view_for_addfld( obj.id ), "img_url" : img_url})
    return res

def make_map( count ):
    if len( count ) > 15:
        return False
    l = count.split( "-" )
    _templ_res = cm.read_file_to_str("html/site-map.html")
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    hrefs = []
    title = "Карта сайта ( {se} )"
    nexthref = False
    if len( l ) < 2:
        #sql = "select count(*) FROM vg_site_db.prices where organization = '{org_id}'".format( org_id = cm.env["organization"].id )
        if count == "":
            index = 0
        else:
            index = int( l[0] )
        se = str( index ) + " - "
        for i in range( 40 ):
            end = "{start}-{end}".format( start = index, end = index + 39 )
            hrefs += [ { "caption": end , "url" : "/site-map/" + end } ]
            index += 40
            if index > cm.env[ "price_count" ]:
                break
        se += str( index - 1 )
        if index < cm.env[ "price_count" ]:
            nexthref = index
        else:
            nexthref = False
    else:
        sql = """
        SELECT caption, fantastic_url FROM vg_site_db.prices 
        where organization = '{org_id}'
        order by insearch desc
        limit {count}, 40;
        """.format( org_id = cm.env["organization"].id, count = l[0] )
        cursor.execute( sql )
        row = cursor.fetchone()
        se = "{a}-{b}".format( a = l[0], b = int( l[0] ) + cursor.rowcount )
        # str( l[0] ) + " - " + str( ( l[0] + cursor.rowcount ) )
        while (row is not None):
            hrefs += [{ "caption": row[0], "url": "/" + row[1] + "/goods" }]
            row = cursor.fetchone()
        cursor.close()
    res = pystache.render( _templ_res, { "hrefs" : hrefs, "nexthref" : nexthref, "title" : title.format( se = se ) } )
    return res

def stat():
    _templ_res = cm.read_file_to_str("html/stat.html")
    s = statistics.stat_info()
    ls = []
    total = 0
    for e in s:
        s[e]["name"] = e
        ls += [s[e]]
        total += s[e]["lines"]
    res = pystache.render(_templ_res, {"stats": ls, "total": total, "dol": total * 12})
    return res

def fetch_to_row_dict( cursor ):
    res = []
    row = cursor.fetchone()

    while row is not None:
        r = {}
        for (i, e) in enumerate(row):
            r[ cursor.description[i][0] ] = e
            pass
        res += [ r ]
        row = cursor.fetchone()
    return res

def orders( url ):
    _templ_res = cm.read_file_to_str("html/orders.html")
    order = dbclasses.dbobj.objects[ "order" ]()
    order.find( id = url )
    partner = dbclasses.dbobj.objects[ "partners" ]()
    partner.find( id = order.partner )
    sql = """
    SELECT * from order_goods where id = %(id)s
    order by count
    """
    db = dbclasses.dbworker.getcon()
    cursor = db.cursor()
    ds = { "id" : url }
    cursor.execute( sql, ds )
    rows = fetch_to_row_dict( cursor )
    totalsum = 0
    for e in rows:
        totalsum += e[ "sum" ]
    #res = pystache.render(_templ_res, { "order" :  , "partner" : partner.__dict__ , "el" : rows, "totalsum" : totalsum , "length" : len(rows) })
    res = pystache.render(_templ_res, { "order" : order.__dict__ , "partner" : partner.__dict__ , "el" : rows, "totalsum" : totalsum , "length" : len(rows) })
    return res