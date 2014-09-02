# -*- coding: utf-8 -*-
import sitedb

def read_file_to_str(filename):
    t = open(filename, "r")
    return t.read()

ldb = sitedb.dbworker()

googs_sql = ldb.class_from_table("goods")