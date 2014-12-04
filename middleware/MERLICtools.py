# -*- coding: utf-8 -*-
import suds
from suds.cache import DocumentCache
import json
import codecs
import common as cm
import urllib

import dbclasses.dbobj
import dbclasses.dbworker
import sett

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

#api_url = "https://api-iz.merlion.ru/mlservice.php?wsdl"
api_url = "https://api.merlion.com/dl/mlservice2?wsdl"
api = suds.client.Client(api_url, username='TC0034492|MPC', password='12345')
api.set_options(cache=DocumentCache())

def fs():
    a = api.service.getShipmentAgents()
    #f = codecs.open("merlion_ShipmentAgents.json", "w", "utf-8")
    f = open("merlion_ShipmentAgents.json", "w")
    f.write(str(a))
    a = api.service.getCurrencyRate()
    f.write(str(a))
    """a = api.service.getShipmentDates()
    f.write(str(a))
    a = api.service.getCatalog()
    f.write(str(a))"""

def load_items(CategoryIDList):
    sql = "delete from prices where synctag = '{id}' and id <> ''".format( id = "merlic " + "N1" )
    cm.ldb.execute(sql)
    org = cm.organization_sql()
    org.find(caption = "ezsp")
    a = api.service.getItems(cat_id = CategoryIDList)
    print "Take {n} item elements".format(n = len(a.item))
    for e in a.item:
        #p = cm.prices_sql()
        #print cm._U(e.Name)
        p = dbclasses.dbobj.objects["prices"]()
        p.caption = cm._U(e.Name)
        p.fantastic_url = urllib.quote(cm._U(e.Name))
        p.item_partner_id = e.No
        p.currency_in = "USD"
        p.organization = org.id.val
        p.synctag = "merlic " + CategoryIDList
        p.write()

def load_price_for_items(CategoryIDList):
    a = api.service.getItemsAvail(shipment_method = u"МПК_ПЕРВЫЙ", shipment_date = "2014-10-28", cat_id = CategoryIDList)
    #p = cm.prices_sql()
    p = dbclasses.dbobj.objects["prices"]()
    print "Take {n} prices elements".format(n = len(a.item))
    for e in a.item:
        if p.find( item_partner_id = e.No ):
            p.price_in = e.PriceClient
            p.price = cm.price_maker( e.PriceClient * 41.9497 * 1.27 )
            if e.PriceClient == 0:
                p.insearch = False
            else:
                p.insearch = True
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

def add_properties( id ):
    p = cm.prices_sql()
    if p.find(item_partner_id = id):
        pr = cm.properties_sql()
        pr.delete( price_id = p.id.val )
        a = api.service.getItemsProperties( item_id = id )
        for e in a.item:
                if e.No is None:
                    continue
                pr = cm.properties_sql()
                pr.price_id = p.id.val
                pr.caption = cm._U(e.PropertyName)
                pr.value = cm._U(e.Value)
                pr.write()

def load_properties_for_items(CategoryIDList):
    sql = "select item_partner_id from prices where sync_tag = '{id}'".format( id = "merlic " + CategoryIDList )
    cursor = cm.ldb.execute(sql)
    pos = 0;
    row = cursor.fetchone()
    while row is not None:
        pos += 1
        add_properties( row[0] )
        row = cursor.fetchone()
        print "{pos} from {r}".format(pos = pos, r = cursor.rowcount)
#

load_items( u"А1" )
load_price_for_items( u"А1" )

#load_img_for_items("N1")
#load_properties_for_items("N1")
#p = cm.properties_sql()
#p.delete( price_id = "59bbc490-3e49-11e4-86cb-4ceb421a4969" )
#add_properties( "934500" )
#load_properties_for_items("N1")
fs()
print "end"