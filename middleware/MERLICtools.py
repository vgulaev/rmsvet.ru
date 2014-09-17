# -*- coding: utf-8 -*-
import suds
from suds.cache import DocumentCache
import json
import codecs
import common as cm
import urllib

#api_url = "https://api-iz.merlion.ru/mlservice.php?wsdl"
api_url = "https://api.merlion.com/dl/mlservice2?wsdl"
api = suds.client.Client(api_url, username='TC0034492|MPC', password='12345')
api.set_options(cache=DocumentCache())

def fs():
    a = api.service.getShipmentAgents()
    f = codecs.open("merlion_ShipmentAgents.json", "w", "utf-8")
    f.write(str(a))
    a = api.service.getCurrencyRate()
    f.write(str(a))
    a = api.service.getShipmentDates()
    f.write(str(a))

def load_items(CategoryIDList):
    sql = "delete from prices where sync_tag = '{id}' and id <> ''".format( id = "merlic " + "N1" )
    cm.ldb.execute(sql)
    org = cm.organization_sql()
    org.find(caption = "ezsp")
    a = api.service.getItems(cat_id = CategoryIDList)
    print "Take {n} item elements".format(n = len(a.item))
    for e in a.item:
        p = cm.prices_sql()
        #print cm._U(e.Name)
        p.caption = cm._U(e.Name)
        p.fantastic_url = urllib.quote(cm._U(e.Name))
        p.item_partner_id = e.No
        p.currency_in = "USD"
        p.organization = org.id.val
        p.sync_tag = "merlic " + CategoryIDList
        p.write()

def load_price_for_items(CategoryIDList):
    a = api.service.getItemsAvail(shipment_method = u"МПК_ПЕРВЫЙ", shipment_date = "2014-09-16", cat_id = CategoryIDList)
    p = cm.prices_sql()
    print "Take {n} prices elements".format(n = len(a.item))
    for e in a.item:
        if p.find(item_partner_id = e.No):
            p.price_in = e.PriceClient
            p.price = cm.price_maker( e.PriceClient * 37.9861 * 1.1 )
            p.write()

def add_img( id ):
    p = cm.prices_sql()
    if p.find(item_partner_id = id):
        a = api.service.getItemsImages( item_id = id )
        #print a, id
        for e in a.item:
                if e.No is None:
                    continue
                img = cm.images_sql()
                img.price_id = p.id.val
                img.url = "http://img.merlion.ru/items/" + e.FileName
                img.write()

def load_img_for_items(CategoryIDList):
    sql = "select item_partner_id from prices where sync_tag = '{id}'".format( id = "merlic " + CategoryIDList )
    cursor = cm.ldb.execute(sql)
    pos = 0;
    row = cursor.fetchone()
    while row is not None:
        pos += 1
        add_img( row[0] )
        row = cursor.fetchone()
        print "{pos} from {r}".format(pos = pos, r = cursor.rowcount)

#sql = "delete from prices where sync_tag = '{id}' and id <> ''".format( id = "merlic " + "N1" )
#print sql
#cm.ldb.execute(sql)

load_items("N1")
load_price_for_items("N1")
load_img_for_items("N1")
print "end"