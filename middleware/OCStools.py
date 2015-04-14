# -*- coding: utf-8 -*-

import requests
import json
import sett
import common as cm
import codecs
import urllib
import datetime
import dbclasses.dbobj
import dbclasses.dbworker
import sett

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

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

def getcatalog():
    payload = {"Login": sett.ocs_login,
           "Token": sett.ocs_token}
    r = requests.post(sett.ocs_srv + "GetCatalog", data=json.dumps(payload), headers=headers)
    f = codecs.open("ocs_catalog.json", "w", "utf-8")
    f.write(r.text)

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
    f = codecs.open("ocs_price.json", "w", "utf-8" )
    f.write(r.text)

crosrate = 62.3649
def load_to_db( CategoryIDList ):
    sql = "delete from prices where synctag = 'ocs {id}'".format( id = CategoryIDList )
    db = dbclasses.dbworker.getcon()
    #cur = cm.currency_sql()
    #cur.find(caption = "USD")
    #crosrate = float(cur.rate.val)
    print( sql )
    cursor = db.cursor()
    cursor.execute( sql )
    db.commit()
    tf = codecs.open( "ocs_price.json", "r", "utf-8" )
    sf = tf.read()
    print( "Try load" )
    s = json.loads( sf )
    print( "Get el by el" )
    #print( crosrate )
    org = dbclasses.dbobj.objects[ "organization" ]()
    org.find( caption = "ezsp" )
    cat = dbclasses.dbobj.objects[ "catalog_ocs" ]()
    cat.find( c_id = "{0}".format( CategoryIDList ) )
    dt_now = datetime.datetime.now()
    dt_for_db = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    for ( i, e ) in enumerate( s["d"]["Products"] ):
        newprice = dbclasses.dbobj.objects["prices"]()
        newprice.caption = e["ItemName"]
        newprice.fantastic_url = urllib.parse.quote( e["ItemName"] )
        #print( e["ItemName"] )
        newprice.organization = org.id
        if e["Currency"] == "USD":
            price = e["Price"] * crosrate * (1 + e["PercentConv"]/100)
        else:
            price = e["Price"]
        newprice.price = cm.price_maker(price * 1.15)
        #print price_maker(price * 1.15), price
        newprice.price_in = e["Price"]
        newprice.currency_in = e["Currency"]
        newprice.synctag = "ocs " + CategoryIDList
        newprice.insearch = True
        newprice.category = cat
        newprice.partner = "ocs"
        newprice.pricedate = dt_for_db
        newprice.vat = 18
        newprice.write()
        inTyumen = False
        for lc in e[ "Locations" ]:
            if lc[ "Location" ] == "Тюмень":
                addfld = dbclasses.dbobj.objects["properties"]()
                addfld.priceref = newprice.id
                addfld.caption = "Срок поставки"
                addfld.value = "В наличии"
                addfld.write()
                inTyumen = True
        if inTyumen == False:
            addfld = dbclasses.dbobj.objects["properties"]()
            addfld.priceref = newprice.id
            addfld.caption = "Срок поставки"
            addfld.value = "Две недели"
            addfld.write()
        if i % 200 == 0:
            print( i )
    print( len( s["d"]["Products"] ) )
"""        ad =  cm.additionalfields_sql()
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
        ad.write()"""

    
def work_loading():
    #currency_sync()
    #l = ["20", "15", "26", "16", "01", "02", "09"]
    l = [ "0901", "20" ]
    for e in l:
        get_price(e)
        load_to_db(e)
#{"CategoryID":"0901","CategoryName":"Ноутбуки","ParentCategoryID":"09","NestingLevel":3},
#getcatalog()
#load_to_db("20")
#work_loading()
#currency_sync()
get_price( "2003" )
#load_to_db( "0901" )

print( "End" )