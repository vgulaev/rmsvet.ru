# -*- coding: utf-8 -*-
import sitedb

import xml.etree.ElementTree as ET

tree = ET.parse('c:/_del/my.xml')
root = tree.getroot()

ldb = sitedb.dbworker()
cg = ldb.class_from_table("goods")
a = cg()
for child in root:
    a.id = child.attrib["ID"]
    a.caption = child.attrib[u"Наименование"]
    a.price = float(child.attrib[u"Цена"].replace(",", "."))
    a.write()

print "Complate"