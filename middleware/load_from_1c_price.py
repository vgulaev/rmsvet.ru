# -*- coding: utf-8 -*-
import sitedb

import xlrd
import common
import MySQLdb
import urllib
import datetime

import dbclasses.dbobj
import dbclasses.dbworker
import sett

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

#common.ldb.create_table();
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
    org = common.organization_sql()
    org.find(caption = "ezsp")
    pos = 0
    for i in range(sheet.nrows - 1):
        if (sheet.cell(i,2).value == u"руб"):
            pr = sheet.cell(i,3).value;
            if not((pr == "*") or (pr == "-") or (pr == "")):
                pos = pos + 1
                
                #newprice = common.prices_sql()
                newprice = dbclasses.dbobj.objects["prices"]()
                newprice.caption = sheet.cell(i,1).value
                newprice.fantastic_url = urllib.quote(common._U(sheet.cell(i,1).value))
                newprice.synctag = "from 1c"
                newprice.organization = org.id.val
                #newprice.price_date = dt_for_db
                newprice.insearch = True;
                if isinstance(pr, unicode):
                    newprice.price = float(pr.replace(unichr(160), u"").replace(",", "."))
                else:
                    newprice.price = pr
                #try:
                newprice.write()
                
                """addfld = common.properties_sql()
                addfld.caption = "__caption__"
                addfld.price_id = str(newprice.id)
                addfld.value = unicode(newprice.caption)
                addfld.write()

                addfld = common.properties_sql()
                addfld.caption = "код прайса 1с"
                addfld.price_id = str(newprice.id)
                addfld.value = sheet.cell(i,0).value
                addfld.write()"""
    print "Loading {p} complate".format(p = pos)

load_from_1c()

#dt_now = datetime.datetime.now()
#print dt_now.strftime('%Y-%m-%d %H:%M:%S')