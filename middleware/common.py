# -*- coding: utf-8 -*-
import sitedb
import codecs


def _U(s):
    res = s
    if isinstance(s, unicode):
        res = s.encode('utf-8')
    return res
        
def _Q(s):
    return "'{s}'".format(s = s)
def read_file_to_str(filename):
    #t = open(filename, "r")
    t = codecs.open(filename, encoding='utf-8')
    return t.read()

ldb = sitedb.dbworker()

googs_sql = ldb.class_from_table("goods")