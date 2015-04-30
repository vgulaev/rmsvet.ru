# -*- coding: utf-8 -*-
import mysql.connector as MySQLdb
import dbclasses.dbmaintenance
import dbclasses.dbworker
import sett
import dbclasses.dbobj
from checon import PyLibCC
from checon import JSLibCC
from checon import CheColl

PyLibCC.CheckInstModD(r"..//middleware")
JSLibCC.CheckInstModD(r"..//middleware")
sql = """SHOW VARIABLES LIKE 'character_sets_dir';"""
db = dbclasses.dbworker.getcon()
cursor = db.cursor()
cursor.execute( sql )
print(cursor._rows[0][1])
CheColl.CheColl(r"{0}".format(cursor._rows[0][1])+"Index.xml")

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

try:
    print( "try DB droping" )
    dbclasses.dbworker.getcon()
    cred = dbclasses.dbworker.cred
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], charset = 'utf8')
    cursor = db.cursor()

    sql = "DROP DATABASE IF EXISTS vg_site_db"
    cursor.execute(sql)
    db.commit()

    print( "DB droped" )
except:
    cred = dbclasses.dbworker.cred
    db = MySQLdb.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], charset = 'utf8')
    cursor = db.cursor()

    sql = "CREATE DATABASE IF NOT EXISTS vg_site_db"
    cursor.execute(sql)
    db.commit()

    dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )
    dbclasses.dbmaintenance.createtable()
    #t.create_table()
    print( "DB preparation complate" )

    p = dbclasses.dbobj.objects[ "partners" ]()
    p.caption = "OCS"
    p.catalog_name = "catalog_ocs"
    p.write()

    o = dbclasses.dbobj.objects[ "organization" ]()
    o.caption = "ezsp"
    o.write()

    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "ezsp.ru"
    p.write()

    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "eazyshop.ru"
    p.write()

    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "127.0.0.1:8080"
    p.write()

    o = dbclasses.dbobj.objects[ "organization" ]()
    o.caption = "rmsvet"
    o.write()

    p = dbclasses.dbobj.objects[ "domains" ]()
    p.organization = o.id
    p.caption = "rmsvet.ru"
    p.write()