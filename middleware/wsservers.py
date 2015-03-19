# -*- coding: utf-8 -*-
import json
import datetime
import common
import dbclasses.dbworker

def debug_my_code(filter):
    res = {"goods": [],
    "lala": str(type(filter)),
        "str" : filter.split(" ")}
    return json.dumps(res)

def make_cond_from_filter( filter ):
    sql = ""
    org = common.env["organization"]
    if len(filter) > 0:
        likes = filter.split(" ")
        likes = ["prices.caption like '%" + e + "%'" for e in likes if e != ""]
        sql += " and ".join(likes)
    if len(sql) > 0:
        sql += "and " 
    sql += """prices.organization = '{org_id}'
    and prices.insearch = 1
    """.format( org_id = org.id )
    return sql

def try_int( one ):
    try:
        res = int( one )
    except:
        res = 0
    return res

def auto_complate( filter, params ):
    sql = """SELECT id, fantastic_url, caption, price FROM vg_site_db.prices
    where
    """
    if "price_from" in params:
        if try_int( params[ "price_from" ] ) > 0:
            sql += " price >=  {price_from} and ".format( price_from = params[ "price_from" ] )
    if "price_to" in params:
        if try_int( params[ "price_to" ] ) > 0:
            sql += " price <=  {price_to} and ".format( price_to = params[ "price_to" ] )
    if "supplier" in params:
        if params[ "supplier" ] != "":
            sql += " partner =  '{supplier}' and ".format( supplier = params[ "supplier" ] )
    sql += make_cond_from_filter( filter )
    if "order_price" in params:
        if params[ "order_price" ] == "asc":
            sql += "order by price asc\n"
        elif params[ "order_price" ] == "desc":
            sql += "order by price desc\n"
    sql += "\n limit 7;" 
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    cursor.execute( sql )
    gd = []
    row = cursor.fetchone()
    while row is not None:
        gd += [{ "id": row[0],
                "fantastic_url": row[1],
                "caption": row[2],
                "price" : str( row[3] ),
                "currency" : "RUR"
                }]
        row = cursor.fetchone()
    cursor.close()
    res = {"goods" : gd}
    return res
    #return json.dumps(res)

def getfilters( filter ):
    sql = """select * from (
    SELECT properties.caption FROM vg_site_db.prices
    join vg_site_db.properties on prices.id = properties.priceref
    where """ + make_cond_from_filter( filter ) + """
    group by properties.caption)
    as cap;"""
    items = []
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    cursor.execute( sql )
    row = cursor.fetchone()
    i = 0
    while row is not None:
        items += [{"index" : i,
                    "name" : row[0],
                    "condition" : "eq",
                    "values" : ""}]
        i += 1
        row = cursor.fetchone()
    res = {"items": items}
    return res

def process( eq ):
    #import time
    #time.sleep( 1 )
    goods = auto_complate( eq["q"], eq["p"] )
    #print( type( eq["p"] ) )
    filters = getfilters( eq["q"] )
    ans = { "q_id" : eq["id"],
            "r" : goods, 
            "f" : filters }
    return ans

def ezspquery( jsonsrt ):
    eq = json.loads( jsonsrt )
    #print( type( jsonobj ) )
    #print( jsonobj )
    ans = process( eq )
    return json.dumps( ans )

def ezsp_get_filters_value ( jsonsrt ):
    sql = """select * from (
    SELECT properties.value FROM vg_site_db.prices
    join vg_site_db.properties on prices.id = properties.priceref
    where """ + make_cond_from_filter( filter ) + """
    
    group by properties.value)
    as cap;"""
    items = []
    cursor = common.ldb.execute(sql)
    row = cursor.fetchone()
    i = 0
    while row is not None:
        items += [{"index" : i,
                    "name" : row[0],
                    "condition" : "eq",
                    "values" : ""}]
        i += 1
        row = cursor.fetchone()
    res = {"items": items}

def getnextordernumber( dt_for_number ):
    org = common.env["organization"]
    sql = "select count(*) from `order` where `order`.number like '{dt}%' and `order`.organization = '{org_id}'".format( org_id = org.id, dt = dt_for_number )
    con = dbclasses.dbworker.getcon()
    cursor = con.cursor()
    cursor.execute( sql )
    row = cursor.fetchone()
    if row is not None:
        res = row[ 0 ] + 1
    else:
        res = 1
    return dt_for_number + "-" + "{0:0>3}".format( str( res ) )

def create_order( jsonstr ):
    rows = json.loads( jsonstr )
    org = common.env["organization"]
    ds = dbclasses.dbobj.objects[ "order" ]()
    dt_now = datetime.datetime.now()
    dt_for_db = dt_now.strftime( '%Y-%m-%d %H:%M:%S' )
    dt_for_number = dt_now.strftime( '%Y%m%d' )
    ds.organization = org.id 
    ds.number = getnextordernumber( dt_for_number )
    ds.date = dt_for_db
    for e in rows:
        newpos = ds.goods.add()
        newpos["good"] = e[ "caption" ]
        newpos["quantity"] = e[ "count" ]
        newpos["price"] = e[ "price" ]
        newpos["sum"] = e[ "sum" ]
        newpos["vat"] = 0
        newpos["vatsum"] = 0
    ds.write()
    ans = { "r" : False }
    if ds.id != "":
        ans = { "r" : True, "id" : ds.id }
    return json.dumps( ans )