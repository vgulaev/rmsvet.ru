# -*- coding: utf-8 -*-
#import MySQLdb
import mysql.connector as MySQLdb

cred = {
        "host" : "",
        "user" : "",
        "pass" : ""
        }

def loadmysqlcredential( psett ):
    passwd = ""
    r = {   "host" : 'localhost',
            "user" : 'root',
            #"passwd" : psett["mysql_pass"]}
            "passwd" : psett.mysql_pass
            }
    return r

def getcon():
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "vg_site_db", charset = 'utf8' )
    return db