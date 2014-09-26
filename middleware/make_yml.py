# -*- coding: utf-8 -*-
import common as cm

import xml.etree.ElementTree as ET
import pystache
import datetime

"""<offer id="{{ yml_id }}" available="true">
    <url>http://eazyshop.ru/{{ url }}/goods</url>
    <price>{{ price }}</price>
    <currencyId>RUR</currencyId>
    <categoryId>1</categoryId>
    <market_category>1047</market_category>
    <store>true</store>
    <pickup>false</pickup>
    <delivery>true</delivery>
    <typePrefix>1С</typePrefix>
    <vendor>1С</vendor>
    <vendorCode>{{ yml_id }}</vendorCode>
</offer>"""
#type="vendor.model" 
templ = """
<offer id="{{ yml_id }}" available="true">
    <url>http://eazyshop.ru/{{ url }}/goods</url>
    <price>{{ price }}</price>
    <currencyId>RUR</currencyId>
    <categoryId>1</categoryId>
    <store>true</store>
    <pickup>false</pickup>
    <delivery>true</delivery>
    <name>{{ name }}</name>
    <vendor>1С</vendor>
    <vendorCode>{{ yml_id }}</vendorCode>
</offer>
"""
#    <description>Программа для ведения бухгалтерского учета</description>
tree = ET.parse('yml.xml')
root = tree.getroot()

shop = root.find("shop")
offers = shop.find("offers")

shop.remove(offers)

offers = ET.Element("offers")

p = cm.properties_sql()
t = cm.prices_sql()

root.set("date", "2014-09-19 17:00")
def add_offers( yml_id ):
    p.find( value = yml_id )
    t.find( id = p.price_id.val )

    if 15 + len(t.fantastic_url.val) > 500:
        print "too length url ", yml_id
    el_str = pystache.render( templ, {"yml_id" : yml_id,
                                      "url" : t.fantastic_url.val,
                                      "price" : t.price,
                                      "name" : t.caption.val} )
    offer = ET.fromstring( el_str )
    offers.append( offer )

el = ["4601546092588", "4601546044433", "4601546041807", "4601546044440", "4601546092595",
      "4601546041814"]
for e in el:
    add_offers( e )

shop.append(offers)
tree.write("yml.xml", encoding="utf-8", xml_declaration = True)
#print of.child.

print "End"