# -*- coding: utf-8 -*-
import pymysql as MySQLdb

cred = {
        "host" : "",
        "user" : "",
        "pass" : ""
        }

def loadmysqlcredential( psett ):
    r = {   "host" : 'localhost',
            "user" : 'root',
            "passwd" : psett.mysql_pass
            }
    return r

def getcon():
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "vg_site_db", charset = 'utf8' )
    return db