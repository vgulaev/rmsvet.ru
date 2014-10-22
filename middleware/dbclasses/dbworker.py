# -*- coding: utf-8 -*-
import MySQLdb
cred = {
        "host" : "",
        "user" : "",
        "pass" : ""
        }
def getcon():
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "vg_site_db", charset = 'utf8')
    return db