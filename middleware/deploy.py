# -*- coding: utf-8 -*-
import MySQLdb
import sitedb

try:
    t = sitedb.dbworker()
    t.connect()
    
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
    
    import common as cm

    p = cm.partners_sql()
    p.caption = "OCS"
    p.write()

    o = cm.organization_sql()
    o.caption = "ezsp"
    o.write()

    p = cm.domains_sql()
    p.organization_id = o.id.val
    p.caption = "ezsp.ru"
    p.write()

    p = cm.domains_sql()
    p.organization_id = o.id.val
    p.caption = "eazyshop.ru"
    p.write()

    p = cm.domains_sql()
    p.organization_id = o.id.val
    p.caption = "127.0.0.1:8080"
    p.write()


    o = cm.organization_sql()
    o.caption = "rmsvet"
    o.write()

    p = cm.domains_sql()
    p.organization_id = o.id.val
    p.caption = "rmsvet.ru"
    p.write()