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

prices_sql = ldb.class_from_table("prices")
additionalfields_sql = ldb.class_from_table("additionalfields")
partners_sql = ldb.class_from_table("partners")
currency_sql = ldb.class_from_table("currency")
images_sql = ldb.class_from_table("images")
domains_sql = ldb.class_from_table("domains")
organization_sql = ldb.class_from_table("organization")
env = {"organization" : None}