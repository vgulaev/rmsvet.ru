# -*- coding: utf-8 -*-
import json
import common

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
        likes = ["prices.caption like '%" + e + "%'" for e in likes if e <> ""]
        sql += " and ".join(likes)
    if len(sql) > 0:
        sql += "and " 
    sql += """prices.organization = '{org_id}'
    and prices.in_search = 'y'
    """.format( org_id = org.id.val )
    return sql

def auto_complate( filter ):
    sql = """SELECT id, fantastic_url, caption, price FROM vg_site_db.prices
    where
    """
    sql += make_cond_from_filter( filter )
    sql += "\n limit 7;" 
    #print sql
    cursor = common.ldb.getcursor()
    cursor.execute(sql)
    gd = []
    row = cursor.fetchone()
    while row is not None:
        gd += [{ "id": row[0],
                "fantastic_url": row[1],
                "caption": row[2],
                "price" : str(row[3]),
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
    join vg_site_db.properties on prices.id = properties.price_id
    where """ + make_cond_from_filter( filter ) + """
    group by properties.caption)
    as cap;"""
    items = []
    cursor = common.ldb.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        items += [row[0]]
        row = cursor.fetchone()
    res = {"items": items}
    return res

def process( eq ):
    res = auto_complate( eq["q"] )
    eq["r"] = res
    res = getfilters( eq["q"] )
    eq["f"] = res
def ezspquery( jsonsrt ):
    eq = json.loads(jsonsrt)
    process( eq )
    return json.dumps(eq)