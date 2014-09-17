# -*- coding: utf-8 -*-
import json
import common

def debug_my_code(filter):
    res = {"goods": [],
    "lala": str(type(filter)),
        "str" : filter.split(" ")}
    return json.dumps(res)

def auto_complate(tbname, filter):
    sql = "SELECT id, fantastic_url, caption, price FROM vg_site_db.prices"
    #return debug_my_code(filter)
    if len(filter) > 0:
        #sql += "\n where MATCH (caption) "
        sql += "\n where "
        likes = filter.split(" ")
        likes = ["caption like '%" + e + "%'" for e in likes if e <> ""]
        #likes = ["'+*" + e + "*'" for e in likes if e <> ""]
        #sql += "AGAINST(" + " ".join(likes) + "  IN BOOLEAN MODE)"
        sql += " and ".join(likes)
    org = common.env["organization"]
    if org is not None:
        sql += "\n and organization = '{org_id}'".format(org_id = org.id.val)
    sql += "\n and in_search = 'y'"
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
    return json.dumps(res)