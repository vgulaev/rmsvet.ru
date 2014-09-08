# -*- coding: utf-8 -*-
import sitedb

import xlrd
import common
import MySQLdb

#common.ldb.create_table();
def load_from_1c():
    rb = xlrd.open_workbook('PRICE_1C.XLS',formatting_info=True)
    sheet = rb.sheet_by_index(0)

    newgood = common.googs_sql()
    pos = 0
    for i in range(sheet.nrows - 1):
        if (sheet.cell(i,2).value == "руб"):
            pos = pos + 1
            pr = sheet.cell(i,3).value;
            if not((pr == "*") or (pr == "-") or (pr == "")):
                newgood = common.googs_sql()
                newgood.caption = unicode(MySQLdb.escape_string(sheet.cell(i,1).value))
                if isinstance(pr, unicode):
                    newgood.price = float(pr.replace(unichr(160), u"").replace(",", "."))
                else:
                    newgood.price = pr
                #try:
                newgood.write()
                #except:
                    #print sheet.cell(i,0).value
                    #print unicode(MySQLdb.escape_string(sheet.cell(i,1).value))
                    #print newgood.caption.str_to_db()
                    #break
                #print sheet.cell(i,1).value
                #print sheet.cell(i,3).value
            #break
    print "Loading {p} complate".format(p = pos)

load_from_1c()