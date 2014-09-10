# -*- coding: utf-8 -*-

import requests
import json
import sett
import common as cm

headers = {'content-type': 'application/json; charset=utf-8'}

def currency_sync():
    payload = {"Login": sett.ocs_login,
           "Token": sett.ocs_token}
    r = requests.post(sett.ocs_srv + "GetCurrentCurrencyRate", data=json.dumps(payload), headers=headers)
    s = json.loads(r.text)
    ocs = cm.partners_sql()
    ocs.find(caption = "ocs")
    
    cur = cm.currency_sql()
    cur.find(partner = ocs.id)
    cur.partner = ocs.id
    cur.caption = "USD"
    cur.rate = s["d"]["Rate"]
    cur.write()

def get_price( CategoryIDList ):
    payload = {"Login": sett.ocs_login,
           "Token": sett.ocs_token,
           "Availability": 1,
           "ShipmentCity": "Тюмень",
           "DisplayMissing": 0,
           "LocationList": [],
           "CategoryIDList" : [CategoryIDList],
           "ItemIDList": []}
    r = requests.post(sett.ocs_srv + "GetProductAvailability", data=json.dumps(payload), headers=headers)
    f = open("ocs_price.json", "w")
    f.write(r.text)

def load_to_db( CategoryIDList ):
    sql = "delete from prices where sync_tag = 'ocs {id}'".format( id = CategoryIDList )
    cm.ldb.execute(sql)
    s = json.loads(cm.read_file_to_str("ocs_price.json"))
    for e in s["d"]["Products"]:
        p = cm.prices_sql()
        p.caption = e["ItemName"]
        p.price = e["Price"]
        p.currency = e["Currency"]
        p.sync_tag = "ocs " + CategoryIDList
        p.write()
        
        ad =  cm.additionalfields_sql()
        ad.caption = "PartNumber"
        ad.price_id = p.id
        ad.value = e["PartNumber"]
        ad.write()
        
        ad =  cm.additionalfields_sql()
        ad.caption = "Producer"
        ad.price_id = p.id
        ad.value = e["Producer"]
        ad.write()
        
        ad =  cm.additionalfields_sql()
        ad.caption = "__ItemID__"
        ad.price_id = p.id
        ad.value = e["ItemID"]
        ad.write()

    print len(s["d"]["Products"])
    
#currency_sync()
l = ["20", "15", "26", "16", "01", "02"]
for e in l:
    get_price(e)
    load_to_db(e)

print "End"