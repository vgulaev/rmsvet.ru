# -*- coding: utf-8 -*-
import xlrd
import common
import datetime
import urllib

#common.ldb.create_table();
def load_from_brom():
    rb = xlrd.open_workbook('brom.xls',formatting_info=True)
    sheet = rb.sheet_by_index(0)

    sql = "delete from prices where sync_tag = 'brom'"
    common.ldb.execute(sql)
    dt_now = datetime.datetime.now()
    dt_for_db = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    pos = 0
    org = common.organization_sql()
    org.find(caption = "rmsvet")
    for i in range(1, sheet.nrows - 1):
        pos += 1
        newprice = common.prices_sql()
        newprice.caption = sheet.cell(i,2).value
        newprice.fantastic_url = urllib.quote(common._U(sheet.cell(i,2).value))
        newprice.price = sheet.cell(i,4).value
        newprice.description = sheet.cell(i,12).value
        newprice.sync_tag = "brom"
        newprice.organization = org.id.val
        newprice.price_date = dt_for_db
        newprice.write()
    print "Loading {p} complate".format(p = pos)

def load_images():
    rb = xlrd.open_workbook('froogle.xls',formatting_info=True)
    sheet = rb.sheet_by_index(0)
    sql = "delete from images where id <> ''"
    common.ldb.execute(sql)
    pos = 0
    price = common.prices_sql()
    for i in range(1, sheet.nrows - 1):
        cap = sheet.cell(i,1).value
        if isinstance(cap, unicode):
            if price.find(caption = cap):
                pos += 1
                img = common.images_sql()
                img.price_id = price.id.val
                img.url = sheet.cell(i,3).value
                img.write()
    print "Loading {p} complate".format(p = pos)


load_from_brom()
load_images()