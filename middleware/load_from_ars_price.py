# -*- coding: utf-8 -*-
import xlrd
import urllib.parse
import math
import datetime
import poplib
import email
import zipfile

import dbclasses.dbobj
import dbclasses.dbworker
import sett

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential(sett)

def load_from_ars( filename ):
    rb = xlrd.open_workbook( filename, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    sql = "delete from prices where synctag = 'from ars' and id <> ''"
    db = dbclasses.dbworker.getcon()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    dt_now = datetime.datetime.now()
    dt_for_db = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    org = dbclasses.dbobj.objects["organization"]()
    org.find(caption="ezsp")
    pos = 0
    for i in range(31, sheet.nrows - 30):
        currency = sheet.cell(i, 2).value
        if not (currency == ''):
            if type(currency) != float:
                currency = float(currency.replace(',', '.'))
            pr = sheet.cell(i, 3).value
            if pr != '':
                if type(pr) != float:
                    pr = float(pr.replace(',', '.'))
                if currency > pr:
                    pos += 1
                    newprice = dbclasses.dbobj.objects["prices"]()
                    newprice.caption = sheet.cell(i, 1).value
                    newprice.fantastic_url = urllib.parse.quote(sheet.cell(i, 1).value)
                    newprice.synctag = "from ars"
                    newprice.organization = org.id
                    newprice.pricedate = dt_for_db
                    newprice.partner = "арс"
                    newprice.vat = 18
                    newprice.insearch = True
                    newprice.price_in = pr
                    newprice.price_in = pr
                    newprice.price = math.ceil( ( currency-pr ) * 0.75 + pr )
                    newprice.write()
                    addfld = dbclasses.dbobj.objects["properties"]()
                    addfld.priceref = newprice.id
                    addfld.caption = "артикул партнера"
                    addfld.value = sheet.cell(i, 0).value
                    addfld.write()
                    if (pos % 200) == 0:
                        print("Complate {p}".format(p=pos))
    print("Loading {p} complate, from {lines}".format(p=pos, lines=sheet.nrows))

def check_subject( index ):
    res = False
    response = mb.top( index, 0 )
    message = email.message_from_bytes( b'\n'.join( response[ 1 ] ) )
    hd = email.header.decode_header( message[ "subject" ] )[ 0 ]
    subject = hd[ 0 ].decode( hd[ 1 ] )
    if "Арсенал" in subject:
        res = index
    return res

def save_attached_file_from_msg( index ):
    res = False
    response = mb.retr( index )
    print( "Start download email" )
    message = email.message_from_bytes( b'\n'.join( response[ 1 ] ) )
    for part in message.walk():
        ct = part.get_content_type()
        print( ct )
        if ct == "application/zip":
            filename = part.get_filename()
            print( "Find {s}".format( s = filename ) )
            fp = open( filename, 'wb')
            fp.write( part.get_payload( decode = 1 ) )
            fp.close
            zp = zipfile.ZipFile( filename, "r" )
            zp.extractall( )
            res = filename[ : -3 ] + "xls"
    return res

def analyse_ms():
    for i in range( min( 10, mbcount ) ):
        if check_subject( i + 1 ) != False:
            filename = save_attached_file_from_msg( i + 1 )
            load_from_ars( filename )
            print( filename )

mb = poplib.POP3_SSL( sett.bpa[ "popserver" ], sett.bpa[ "port" ] )
mb.user( sett.bpa[ "user" ] ) 
mb.pass_( sett.bpa[ "pswd" ] )

( mbcount, mbsize ) = mb.stat()
analyse_ms()