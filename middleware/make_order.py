# -*- coding: utf-8 -*-

import dbclasses.dbworker
import dbclasses.dbobj
import sett
import common
import datetime

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

common.detect_common_env()
org = common.env["organization"]

newprice = dbclasses.dbobj.objects["prices"]()
f = newprice.find( caption = """1С:Предприятие 8. Конфигурация "ERP управление предприятием 2.0". 6-е издание (в трех частях)""" )
print( f )

newpartners = dbclasses.dbobj.objects["partners"]()

if newpartners.find( caption = "Частное лицо" ) == False:
    newpartners.caption = "Частное лицо"
    newpartners.write()

#print( newpartners.caption )
#newprice = dbclasses.dbobj.objects["prices"]()

dt_now = datetime.datetime.now()
dt_for_db = dt_now.strftime( '%Y-%m-%d %H:%M:%S' )

neworder = dbclasses.dbobj.objects["order"]()
neworder.organization = org.id
neworder.date = dt_for_db
neworder.number = dt_now.strftime( '%Y%m%d' ) + "-001"
neworder.partner = newpartners.id

newpos = neworder.goods.add()
newpos["good"] = newprice.caption
newpos["quantity"] = 1
newpos["price"] = 900
newpos["sum"] = 900

if newprice.find( caption = """Доставка Тюмень - Москва""" ) == False:
    newprice.caption = "Доставка Тюмень - Москва"
    newprice.price = 960
    newprice.write()

newpos = neworder.goods.add()
newpos["good"] = newprice.caption
newpos["quantity"] = 1
newpos["price"] = 960
newpos["sum"] = 960

neworder.write()
print( neworder.id )

print( newprice.price )
print( "End" )