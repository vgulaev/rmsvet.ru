# -*- coding: utf-8 -*-

import requests
import json
import sett
import common as cm

headers = {'content-type': 'application/json; charset=utf-8'}
#payload = {'Login': 'PYpjGUZKz', 'Token': 'dLxX&p^scYYsWrAt&UdhRxMBMGfXrN'}
#urlgc = "https://b2btestservice.ocs.ru/b2bjson.asmx/GetCatalog"
#urlpa = "https://b2btestservice.ocs.ru/b2bjson.asmx/GetProductAvailability"

"""payload = {"Login": sett.ocs_login,
           "Token": sett.ocs_token,
           "Availability": 1,
           "ShipmentCity": "Тюмень",
           "DisplayMissing": 0,
           "LocationList": [],
           #"CategoryIDList" : ["20"],
           "CategoryIDList" : [],
           "ItemIDList": ["1000122597"]}
r = requests.post(urlpa, data=json.dumps(payload), headers=headers)"""
#print(r.text)
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
        
    print len(s["d"]["Products"])
    
#currency_sync()
get_price("20")
load_to_db("20")
get_price("15")
load_to_db("15")

print "End"