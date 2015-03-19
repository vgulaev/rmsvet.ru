# -*- coding: utf-8 -*-

import xlrd
import common
import urllib
import datetime
from os import remove as rem
import dbclasses.dbobj
import dbclasses.dbworker
import sett

import sys
print( sys.version )

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

def load_from_1c():
    rb = xlrd.open_workbook('PRICE_1C.XLS',formatting_info=True)
    sheet = rb.sheet_by_index(0)

    sql = "delete from prices where synctag = 'from 1c' and id <> ''"
    db = dbclasses.dbworker.getcon()
    cursor = db.cursor()
    cursor.execute( sql )
    db.commit()
    dt_now = datetime.datetime.now()
    dt_for_db = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    org = dbclasses.dbobj.objects[ "organization" ]()
    org.find( caption = "ezsp" )
    pos = 0
    for i in range(sheet.nrows - 1):
        currency = sheet.cell(i,2).value
        if (currency == "руб") or (currency == "руб."):
            pr = sheet.cell(i,3).value;
            if not((pr == "*") or (pr == "-") or (pr == "")):
                pos = pos + 1
                newprice = dbclasses.dbobj.objects["prices"]()
                newprice.caption = sheet.cell(i,1).value
                #print( type( sheet.cell(i,1).value ) )
                newprice.fantastic_url = urllib.parse.quote( sheet.cell(i,1).value )
                newprice.synctag = "from 1c"
                newprice.organization = org.id
                vat = sheet.cell( i, 6 ).value
                if vat == "18%":
                    newprice.vat = 18
                else:
                    newprice.vat = 0
                newprice.pricedate = dt_for_db
                newprice.partner = "софт"
                newprice.insearch = True;
                newprice.price_in = 0
                if isinstance(pr, str):
                    newprice.price = float( pr.replace( chr(160), "" ).replace(",", ".") )
                else:
                    newprice.price = pr
                #try:
                newprice.write()
                
                addfld = dbclasses.dbobj.objects["properties"]()
                addfld.priceref = newprice.id
                addfld.caption = "код прайса 1с"
                addfld.value = sheet.cell(i,0).value
                addfld.write()

                if (pos % 200) == 0:
                    print( "Complate {p}".format( p = pos ) )

    print( "Loading {p} complate, from {lines}".format( p = pos, lines = sheet.nrows ) )

import wget
import zipfile
def get_price_from_web():
    url = "http://www.1c.ru/ftp/pub/pricelst/price_1c.zip"
    filename = wget.download(url)
    print( "Ok" )
    print( filename )
    zp = zipfile.ZipFile( filename, "r" )
    zp.extractall( )

get_price_from_web()
load_from_1c()
rem("price_1c.zip")