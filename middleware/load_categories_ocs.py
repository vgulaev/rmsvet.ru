# -*- coding: utf-8 -*-

import json
from structures import Tree
import dbclasses.dbobj
import dbclasses.dbworker
import sett
import codecs
import OCStools

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )
OCStools.getcatalog()
file = codecs.open ("ocs_catalog.json" , "r", "utf-8")
a = json.loads ( file.read() )
ocsCatalog = a["d"]["Categories"]
print (ocsCatalog)
OCS = Tree.CatalogTree(Parent = "", CID = "", CN = "", Level = 0)
flag = False
#Make catalogs Tree for OCS
#<CAUTION! Make a recursive call!!!>
for i in ocsCatalog:
    if i["NestingLevel"] == 1:
        OCS.addChild( ParentID = i["ParentCategoryID"], CID = i["CategoryID"],  CN = i["CategoryName"] )
    elif i["NestingLevel"] == 2:
        for j in OCS.Child:
            if j.CategoryID == i["ParentCategoryID"]:
                j.addChild( ParentID = i["ParentCategoryID"], CID = i["CategoryID"],  CN = i["CategoryName"] )
                break
    elif i["NestingLevel"] == 3:
        for j in OCS.Child:
            for k in j.Child:
                if k.CategoryID == i["ParentCategoryID"]:
                    k.addChild( ParentID = i["ParentCategoryID"], CID = i["CategoryID"],  CN = i["CategoryName"] )
                    break
            if flag:
                break
    elif i["NestingLevel"] == 4:
        for j in OCS.Child:
            for k in j.Child:
                for l in k.Child:
                    if l.CategoryID == i["ParentCategoryID"]:
                        l.addChild( ParentID = i["ParentCategoryID"], CID = i["CategoryID"],  CN = i["CategoryName"] )
                        flag = True
                        break
            if flag:
                break
        if flag:
            break
    elif i["NestingLevel"] == 5:
        for j in OCS.Child:
            for k in j.Child:
                for l in k.Child:
                    for p in l.Child:
                        if l.CategoryID == i["ParentCategoryID"]:
                            l.addChild( ParentID = i["ParentCategoryID"], CID = i["CategoryID"],  CN = i["CategoryName"] )
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
#</CAUTION! Make a recursive call!!!>
def load_cat_to_db(r=Tree.CatalogTree):
    childs=len(r.Child)
    dbcat = dbclasses.dbobj.objects["catalog_ocs"]()
    dbcat.cat_name = r.CategoryName
    dbcat.c_id = r.CategoryID
    dbcat.nesting_level = r.NestingLevel
    dbcat.parent_c_id = r.ParentCategoryID
    dbcat.write()
    if childs>0:
        for i in range(childs):
            load_cat_to_db(r.Child[i])
#<Cleaning catalog_ocs table>
sql = "TRUNCATE TABLE catalog_ocs"
db = dbclasses.dbworker.getcon()
cursor = db.cursor()
cursor.execute( sql )
#</>
#<Make category from catalog_ocs>
load_cat_to_db(OCS)
#</>
def dfs_getprice(r=Tree.CatalogTree):
    if r.flag1:
        childs=len(r.Child)
        if childs>0:
            for i in range(childs):
                dfs_getprice(r.Child[i])
        else:
            OCStools.get_price( "{0}".format( r.CategoryID ) )
            OCStools.load_to_db( "{0}".format( r.CategoryID ) )
    r.flag1 = False
#<Make prices from 'prices' table>
dfs_getprice(OCS)
#</>
print(OCS.Child[0].CategoryName)
