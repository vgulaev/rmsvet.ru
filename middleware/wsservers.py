# -*- coding: utf-8 -*-
import json
import common

def debug_my_code(filter):
    res = {"goods": [],
    "lala": str(type(filter)),
        "str" : filter.split(" ")}
    return json.dumps(res)

def auto_complate(tbname, filter):
    sql = "SELECT id, caption, price FROM vg_site_db.prices"
    #return debug_my_code(filter)
    if len(filter) > 0:
        sql += "\n where \n"
        likes = filter.split(" ")
        likes = ["caption like '%" + e + "%'" for e in likes if e <> ""]
        sql += " and ".join(likes)
    sql += "\n limit 7;" 
    #print sql
    common.ldb.execute(sql)
    gd = []
    row = common.ldb.cursor.fetchone()
    while row is not None:
        gd += [{ "id": row[0],
                "caption": row[1],
                "price" : str(row[2]),
                "currency" : "RUR"
                }]
        row = common.ldb.cursor.fetchone()
    res = {"goods" : gd}
    return json.dumps(res)