# -*- coding: utf-8 -*-
import MySQLdb
import sitedb

try:
    t = sitedb.dbworker()
    
    cred = sitedb.loadmysqlcredential()
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], charset = 'utf8')
    cursor = db.cursor()
    
    sql = "DROP DATABASE IF EXISTS vg_site_db"
    cursor.execute(sql)
    db.commit()
    
    print "DB droped"
except:
    cred = sitedb.loadmysqlcredential()
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], charset = 'utf8')
    cursor = db.cursor()
    
    sql = "CREATE DATABASE IF NOT EXISTS vg_site_db"
    cursor.execute(sql)
    db.commit()
    
    t = sitedb.dbworker()
    t.create_table()
    print "DB preparation complate"