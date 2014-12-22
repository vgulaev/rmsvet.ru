# -*- coding: utf-8 -*-
import common as cm

import xml.etree.ElementTree as ET
import datetime
import sett

import dbclasses.dbworker

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

dt_now = datetime.datetime.now()
dt_for_xml = dt_now.strftime( '%Y-%m-%d' )

urlset = ET.Element( "urlset", attrib = { "xmlns" : "http://www.sitemaps.org/schemas/sitemap/0.9" } )

con = dbclasses.dbworker.getcon()
cursor = con.cursor()

sql = """select fantastic_url, id from prices"""
cursor.execute( sql )

lastmod = ET.Element( "lastmod" )
lastmod.text = dt_for_xml
priority = ET.Element( "priority" )
priority.text = "0.8"

k = 0
row = cursor.fetchone()
while row is not None:
    url = ET.Element( "url" )
    loc = ET.Element( "loc" )
    if len( row[ 0 ] ) < 200:
        loc.text = "http://eazyshop.ru/" + row[ 0 ] + "/goods"
    else:
        loc.text = "http://eazyshop.ru/catalog/goods/" + row[ 1 ]
    
    url.append( loc )
    url.append( lastmod )
    url.append( priority )
    
    urlset.append( url )
    k += 1
    if k % 100 == 0 :
        print( k )
    row = cursor.fetchone()
    #if k > 3:
    #    break


tree = ET.ElementTree( element = urlset )

tree.write("sitemap.xml", encoding="utf-8", xml_declaration = True)

#print of.child.

print( "End" )